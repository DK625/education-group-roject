from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import logging

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        
        # Locators
        self.email_input = (By.CSS_SELECTOR, ".css-y9vvym-MuiButtonBase-root-MuiButton-root")
        self.password_input = (By.CSS_SELECTOR, "input[name='password']")
        self.login_button = (By.CSS_SELECTOR, "button[type='submit']")
        self.error_message = (By.CSS_SELECTOR, ".error-message")

    def login(self, email, password):
        """Thực hiện login"""
        try:
            self.driver.get("http://localhost:3000/home")
            self.driver.set_window_size(1846, 1053)
            element = self.driver.find_element(By.CSS_SELECTOR, ".css-y9vvym-MuiButtonBase-root-MuiButton-root")
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            self.driver.find_element(By.CSS_SELECTOR, ".css-y9vvym-MuiButtonBase-root-MuiButton-root").click()
            self.driver.find_element(By.ID, ":re:").send_keys("doanthuyduong2103@gmail.com")
            self.driver.find_element(By.ID, ":rf:").send_keys("Thanhthuy2103@")
            self.driver.find_element(By.CSS_SELECTOR, ".MuiButton-root").click()

            # Đợi cho đến khi login thành công (URL thay đổi hoặc element nào đó xuất hiện)
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.current_url != 'http://localhost:3000/login'
            )
            
            return True
            
        except Exception as e:
            self.logger.error(f"Login failed: {str(e)}")
            return False

    def is_logged_in(self):
        """Kiểm tra đã login hay chưa"""
        try:
            # Kiểm tra element chỉ xuất hiện khi đã login
            WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".MuiBox-root.css-5nwj3y"))
            )
            return True
        except:
            return False