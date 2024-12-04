from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC


class TestTest():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_login(self):
        self.driver.get("http://localhost:3000/home")
        self.driver.set_window_size(1846, 1053)

        # Đợi và hover vào nút login
        login_button = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".css-y9vvym-MuiButtonBase-root-MuiButton-root"))
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(login_button).perform()

        # Đợi nút login có thể click được
        login_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".css-y9vvym-MuiButtonBase-root-MuiButton-root"))
        )
        login_button.click()

        # Đợi và điền email
        email_field = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, ":re:"))
        )
        email_field.send_keys("doanthuyduong2103@gmail.com")

        # Đợi và điền password
        password_field = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, ":rf:"))
        )
        password_field.send_keys("Thanhthuy2103@")

        # Đợi và click nút submit
        submit_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".MuiButton-root"))
        )
        submit_button.click()

        try:
            avatar = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".MuiBadge-root.css-h8me6z-MuiBadge-root"))
            )
            # Nếu tìm thấy avatar, test pass
            assert avatar.is_displayed(), "Login failed - Avatar not visible after login"
            print("Login test passed - Avatar found")
            print("Test case passed! ✅")
        except:
            # Nếu không tìm thấy avatar, test fail
            print("Login test failed - Avatar not found")
            raise AssertionError("Login failed - Avatar not found after 30 seconds")
        finally:
            self.driver.close()
