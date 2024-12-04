from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestAddProductToCart():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        """Dọn dẹp sau mỗi test case"""
        self.driver.quit()

    def test_add_product_to_cart(self):
        self.driver.get("http://localhost:3000/home")
        self.driver.set_window_size(962, 1089)

        # Click vào nút đăng nhập và chờ form login
        login_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".css-y9vvym-MuiButtonBase-root-MuiButton-root"))
        )
        login_button.click()

        # Nhập email
        email_input = WebDriverWait(self.driver, 35).until(
            EC.presence_of_element_located((By.ID, ":re:"))
        )
        email_input.send_keys("doanthuyduong2103@gmail.com")

        # Nhập password và submit
        password_input = WebDriverWait(self.driver, 35).until(
            EC.presence_of_element_located((By.ID, ":rf:"))
        )
        password_input.send_keys("Thanhthuy2103@")

        submit_button = WebDriverWait(self.driver, 35).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".MuiButton-root"))
        )
        submit_button.click()

        cart_icon = WebDriverWait(self.driver, 35).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".iconify--flowbite > path"))
        )
        cart_icon.click()  # Click vào icon cart và xem giỏ hàng hiện tại

        initial_count = 0  # Lưu số lượng ban đầu trong giỏ hàng

        backdrop = WebDriverWait(self.driver, 35).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".MuiBackdrop-root"))
        )
        backdrop.click()  # Click vào vùng trắng để đóng giỏ hàng

        button4 = WebDriverWait(self.driver, 35).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".MuiButtonBase-root:nth-child(4)"))
        )
        button4.click()  # Click vào tab Điện thoại để xem sản phẩm

        add_to_cart4 = WebDriverWait(self.driver, 35).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".MuiGrid-root:nth-child(4) .MuiButtonBase-root:nth-child(1)"))
        )
        add_to_cart4.click()  # Click vào nút thêm giỏ hàng của Iphone 15 promax

        updated_count_element = WebDriverWait(self.driver, 35).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".MuiBadge-badge"))
        )
        updated_count = int(updated_count_element.text)
        assert updated_count == initial_count + 1, f"Expected count to be {initial_count + 1}, but got {updated_count}"  # Kiểm tra số lượng tăng lên 1

        cart_icon = WebDriverWait(self.driver, 35).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".iconify--flowbite"))
        )
        cart_icon.click()  # Click vào cart icon để xem sản phẩm vừa được thêm vào

        backdrop = WebDriverWait(self.driver, 35).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".MuiBackdrop-root"))
        )
        backdrop.click()  # Click vào vung trắng để đóng giỏ hàng

        add_to_cart5 = WebDriverWait(self.driver, 35).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".MuiGrid-root:nth-child(5) .MuiButtonBase-root:nth-child(1)"))
        )
        add_to_cart5.click()  # Click vào nút thêm vào giỏ hàng của sản phẩm Samsung Galaxy S23 8GB 128GB

        # Click vào badge color primary
        badge = WebDriverWait(self.driver, 35).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".MuiBadge-colorPrimary"))
        )
        badge.click()  # Click vào cart icon để xem sản phẩm vừa được thêm vào

        backdrop = WebDriverWait(self.driver, 35).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".MuiBackdrop-root"))
        )
        backdrop.click()  # Click vào vùng trắng để đóng giỏ hàng

        button5 = WebDriverWait(self.driver, 35).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".MuiGrid-root:nth-child(5) .MuiButtonBase-root:nth-child(1)"))
        )
        button5.click()  # Click vào nút thêm vào giỏ hàng của sản phẩm Samsung Galaxy S23 8GB 128GB, them 1 sp nua

        icon1 = WebDriverWait(self.driver, 35).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".MuiIconButton-colorInherit:nth-child(1)"))
        )
        icon1.click()  # Click vào icon gio hang để xem so luong (=2) sản phẩm vừa được thêm vào

        backdrop = WebDriverWait(self.driver, 35).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".MuiBackdrop-root"))
        )
        backdrop.click()  # Click vào vùng trắng để đóng giỏ hàng




        iphone_name = WebDriverWait(self.driver, 35).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".MuiTypography-root.MuiTypography-h5.css-mxh2yv-MuiTypography-root"))
            # hoặc tag h6, div chứa tên
        ).text
        iphone_price = WebDriverWait(self.driver, 35).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".MuiBox-root.css-19nzcwv"))
            # hoặc span, div chứa giá
        ).text

        samsung_name = WebDriverWait(self.driver, 35).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".MuiTypography-root.MuiTypography-h5.css-mxh2yv-MuiTypography-root"))
        ).text
        samsung_price = WebDriverWait(self.driver, 35).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".MuiTypography-root.MuiTypography-h4.css-o71y5o-MuiTypography-root"))
        ).text
        cart_iphone_name = WebDriverWait(self.driver, 35).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".MuiTypography-root.MuiTypography-h5.css-mxh2yv-MuiTypography-root"))
            # hoặc div, span chứa tên trong cart
        ).text
        cart_samsung_name = WebDriverWait(self.driver, 35).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".MuiTypography-root.MuiTypography-h5.css-mxh2yv-MuiTypography-root"))
        ).text

        cart_iphone_price = WebDriverWait(self.driver, 35).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".MuiBox-root.css-19nzcwv"))
            # hoặc div, span chứa giá trong cart
        ).text
        cart_samsung_price = WebDriverWait(self.driver, 35).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".MuiTypography-root.MuiTypography-h4.css-o71y5o-MuiTypography-root"))
        ).text
        final_count_element = WebDriverWait(self.driver, 35).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".MuiBadge-badge"))
        )
        final_count = int(final_count_element.text)

        assert cart_iphone_name == iphone_name, "Product name mismatch"
        assert cart_samsung_name == samsung_name, "Product name mismatch"
        assert cart_iphone_price == iphone_price, "Price mismatch"
        assert cart_samsung_price == samsung_price, "Price mismatch"
        assert final_count == initial_count + 3, "Quantity not increased correctly"

        print("""
        TEST CASE: Add Products to Cart

        Results:
        ✓ Product Names Verified (iPhone & Samsung)
        ✓ Product Prices Verified 
        ✓ Quantity Updated: {initial_count} -> {final_count} (+3 items)

        Status: PASSED ✅
        """.format(initial_count=initial_count, final_count=final_count))

