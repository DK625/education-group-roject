from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base import BasePage

class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # Locators
        self.product_checkboxes = (By.CSS_SELECTOR, "input[type='checkbox'].select-item")
        self.product_images = (By.CSS_SELECTOR, ".cart-product-image img") 
        self.product_names = (By.CSS_SELECTOR, ".cart-product-name")
        self.product_prices = (By.CSS_SELECTOR, ".cart-product-price")
        self.quantity_inputs = (By.CSS_SELECTOR, ".quantity-input")
        self.increase_buttons = (By.CSS_SELECTOR, "button.increase-quantity")
        self.decrease_buttons = (By.CSS_SELECTOR, "button.decrease-quantity")
        self.delete_buttons = (By.CSS_SELECTOR, "button.delete-item")
        self.total_amount = (By.CSS_SELECTOR, ".total-amount")
        self.cart_count = (By.CSS_SELECTOR, ".MuiBadge-badge")
        self.select_all = (By.CSS_SELECTOR, "input[type='checkbox'].select-all")


    def get_cart_count(self):
        """Lấy số lượng sản phẩm trong giỏ hàng"""
        element = self.driver.find_element(*self.cart_count)
        return int(element.text)

    def check_product(self, index):
        """Chọn checkbox sản phẩm theo index"""
        checkboxes = self.driver.find_elements(*self.product_checkboxes)
        if not checkboxes[index].is_selected():
            checkboxes[index].click()

    def get_product_info(self, index):
        """Lấy thông tin sản phẩm theo index"""
        images = self.driver.find_elements(*self.product_images)
        names = self.driver.find_elements(*self.product_names)
        prices = self.driver.find_elements(*self.product_prices)
        
        return {
            'image_src': images[index].get_attribute('src'),
            'name': names[index].text,
            'price': self.convert_price_to_number(prices[index].text)
        }

    def increase_quantity(self, index):
        """Tăng số lượng sản phẩm"""
        buttons = self.driver.find_elements(*self.increase_buttons)
        buttons[index].click()
        return self.get_quantity(index)

    def decrease_quantity(self, index):
        """Giảm số lượng sản phẩm"""
        buttons = self.driver.find_elements(*self.decrease_buttons)
        buttons[index].click()
        return self.get_quantity(index)

    def get_quantity(self, index):
        """Lấy số lượng hiện tại của sản phẩm"""
        inputs = self.driver.find_elements(*self.quantity_inputs)
        return int(inputs[index].get_attribute('value'))

    def delete_product(self, index):
        """Xóa sản phẩm khỏi giỏ hàng"""
        initial_count = self.get_cart_count()
        buttons = self.driver.find_elements(*self.delete_buttons)
        buttons[index].click()
        WebDriverWait(self.driver, 10).until(
            lambda driver: self.get_cart_count() < initial_count
        )

    def get_total_amount(self):
        """Lấy tổng tiền của các sản phẩm đã chọn"""
        element = self.driver.find_element(*self.total_amount)
        return self.convert_price_to_number(element.text)

    def convert_price_to_number(self, price_text):
        """Chuyển đổi text giá tiền sang số"""
        return float(price_text.replace('VND', '').replace(',', '').strip())
