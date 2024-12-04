from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.base import BasePage
import logging

class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        """Khởi tạo ProductPage với các locators"""
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        
        # Định nghĩa các locators
        self.product_items = (By.CSS_SELECTOR, ".MuiGrid-item") # Card sản phẩm
        self.product_names = (By.CSS_SELECTOR, ".MuiTypography-h6")  # Tên sản phẩm
        self.product_prices = (By.CSS_SELECTOR, ".product-price") # Giá sản phẩm  
        self.add_to_cart_buttons = (By.CSS_SELECTOR, "button[aria-label='Add to Cart']") # Nút thêm vào giỏ
        self.cart_count = (By.CSS_SELECTOR, ".MuiBadge-badge") # Số lượng trong giỏ
        self.cart_icon = (By.CSS_SELECTOR, "[aria-label='shopping cart']") # Icon giỏ hàng
        
    def wait_for_element(self, locator, timeout=10):
        """Chờ đợi element xuất hiện"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except TimeoutException:
            self.logger.error(f"Element {locator} not found after {timeout} seconds")
            return False
            
    def add_to_cart(self, index=0):
        """Thêm sản phẩm vào giỏ hàng theo index"""
        try:
            if not self.wait_for_element(self.add_to_cart_buttons):
                raise Exception("Add to cart buttons not found")
                
            buttons = self.driver.find_elements(*self.add_to_cart_buttons)
            if not buttons:
                raise Exception("No products available")
                
            # Lưu số lượng ban đầu trong giỏ hàng
            initial_count = self.get_cart_count()
            
            # Click nút thêm vào giỏ
            buttons[index].click()
            
            # Chờ số lượng trong giỏ tăng lên
            WebDriverWait(self.driver, 10).until(
                lambda d: self.get_cart_count() > initial_count
            )
            
            return True
        except Exception as e:
            self.logger.error(f"Error adding product to cart: {e}")
            return False
            
    def get_cart_count(self):
        """Lấy số lượng sản phẩm trong giỏ hàng"""
        try:
            count_element = self.driver.find_element(*self.cart_count)
            return int(count_element.text)
        except:
            return 0
            
    def get_product_info(self, index=0):
        """Lấy thông tin sản phẩm theo index"""
        try:
            if not self.wait_for_element(self.product_items):
                return None
                
            names = self.driver.find_elements(*self.product_names)
            prices = self.driver.find_elements(*self.product_prices)
            
            return {
                'name': names[index].text,
                'price': self.convert_price_to_number(prices[index].text)
            }
        except Exception as e:
            self.logger.error(f"Error getting product info: {e}")
            return None
            
    def convert_price_to_number(self, price_text):
        """Chuyển đổi text giá tiền sang số"""
        try:
            return float(price_text.replace('VND', '').replace(',', '').strip())
        except:
            return 0.0
            
    def verify_add_to_cart(self, index=0):
        """Kiểm tra thêm vào giỏ hàng thành công"""
        initial_count = self.get_cart_count()
        if self.add_to_cart(index):
            new_count = self.get_cart_count()
            return new_count > initial_count
        return False