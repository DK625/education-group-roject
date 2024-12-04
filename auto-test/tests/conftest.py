import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import os
from datetime import datetime
from pages.cart_page import CartPage
from pages.product_page import ProductPage
from pages.login_page import LoginPage


def pytest_addoption(parser):
    """Add command-line options"""
    parser.addoption("--browser", action="store", default="chrome", help="browser to run tests (chrome/firefox)")
    parser.addoption("--headless", action="store_true", help="run browser in headless mode")


@pytest.fixture(scope="session")
def base_url():
    """Fixture cho base URL"""
    return "http://localhost:3000"


@pytest.fixture
def browser(request):
    """Fixture để lấy tên browser từ command line"""
    return request.config.getoption("--browser")


@pytest.fixture
def headless(request):
    """Fixture để lấy mode headless từ command line"""
    return request.config.getoption("--headless")


@pytest.fixture
def driver(browser, headless):
    """Fixture để khởi tạo WebDriver"""
    if browser.lower() == "chrome":
        chrome_options = Options()
        if headless:
            chrome_options.add_argument('--headless=new')
        chrome_options.add_argument('--start-maximized')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')

        # Sử dụng ChromeDriverManager để tự động tải và quản lý ChromeDriver
        try:
            service = Service('/usr/bin/chromedriver')
            driver = webdriver.Chrome(service=service, options=chrome_options)
            # driver = webdriver.Chrome()
        except Exception as e:
            print(f"Error initializing Chrome driver: {e}")
            raise
    else:
        raise ValueError(f"Browser {browser} is not supported")

    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture
def cart_page(login_first, driver, base_url):
    """Fixture khởi tạo CartPage (sau khi đã login)"""
    driver.get(f"{base_url}/my-cart")
    return CartPage(driver)


@pytest.fixture
def product_page(login_first, driver, base_url):
    """Fixture khởi tạo ProductPage (sau khi đã login)"""
    driver.get(f"{base_url}/home")
    return ProductPage(driver)


@pytest.fixture(autouse=True)
def screenshot_on_failure(request, driver):
    """Fixture để chụp ảnh khi test fail"""
    yield

    # Chỉ chụp ảnh khi test thực sự fail
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        screenshot_dir = "screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)

        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        screenshot_path = os.path.join(
            screenshot_dir,
            f"fail_{request.node.name}_{timestamp}.png"
        )

        driver.save_screenshot(screenshot_path)
        print(f"\nScreenshot saved as {screenshot_path}")


@pytest.fixture(scope="session")
def test_data():
    """Fixture cung cấp test data"""
    return {
        'valid_product': {
            'name': 'Apple Watch Series 9',
            'price': 3790000,
            'quantity': 1
        },
        'max_quantity': 10,
        'min_quantity': 1
    }


def pytest_configure(config):
    """Cấu hình pytest"""
    # Thêm custom markers
    config.addinivalue_line("markers", "cart: cart related tests")
    config.addinivalue_line("markers", "ui: ui related tests")
    config.addinivalue_line("markers", "smoke: smoke tests")
    config.addinivalue_line("markers", "regression: regression tests")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook để bắt status của test case"""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)


@pytest.fixture(scope="session")
def login_data():
    """Fixture cung cấp thông tin đăng nhập"""
    return {
        'email': 'doanthuyduong2103@gmail.com',
        'password': 'Thanhthuy2103@'
    }


@pytest.fixture
def login_page(driver, base_url):
    """Fixture khởi tạo LoginPage"""
    driver.get(f"{base_url}/login")
    return LoginPage(driver)


@pytest.fixture(autouse=True)
def login_first(login_page, login_data):
    """Fixture tự động login trước khi chạy test"""
    if not login_page.is_logged_in():
        assert login_page.login(login_data['email'], login_data['password']), "Login failed"
    yield
