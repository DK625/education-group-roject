import pytest
from pages.cart_page import CartPage

class TestCart:
    @pytest.fixture
    def cart_page(self, driver):
        return CartPage(driver)

    def test_add_product_to_cart(self, cart_page, product_page):
        """Test thêm sản phẩm vào giỏ hàng"""
        initial_count = cart_page.get_cart_count()
        product_page.add_to_cart()
        assert cart_page.get_cart_count() == initial_count + 1

    def test_product_info_display(self, cart_page):
        """Test hiển thị thông tin sản phẩm"""
        product_info = cart_page.get_product_info(0)
        assert product_info['image_src'] is not None
        assert product_info['name'] != ''
        assert product_info['price'] > 0

    def test_increase_quantity(self, cart_page):
        """Test tăng số lượng sản phẩm"""
        initial_quantity = cart_page.get_quantity(0)
        new_quantity = cart_page.increase_quantity(0)
        assert new_quantity == initial_quantity + 1

    def test_decrease_quantity(self, cart_page):
        """Test giảm số lượng sản phẩm"""
        # Đảm bảo số lượng > 1 trước khi test
        cart_page.increase_quantity(0)
        initial_quantity = cart_page.get_quantity(0)
        new_quantity = cart_page.decrease_quantity(0)
        assert new_quantity == initial_quantity - 1

    def test_delete_product(self, cart_page):
        """Test xóa sản phẩm"""
        initial_count = cart_page.get_cart_count()
        cart_page.delete_product(0)
        assert cart_page.get_cart_count() == initial_count - 1

    def test_total_amount_calculation(self, cart_page):
        """Test tính tổng tiền"""
        # Chọn sản phẩm đầu tiên
        cart_page.check_product(0)
        product_info = cart_page.get_product_info(0)
        quantity = cart_page.get_quantity(0)
        expected_total = product_info['price'] * quantity
        assert cart_page.get_total_amount() == expected_total