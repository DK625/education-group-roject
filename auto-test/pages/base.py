import logging
from pages.login_page import LoginPage
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    def ensure_logged_in(self):
        """Đảm bảo đã login trước khi thao tác"""
        if not LoginPage(self.driver).is_logged_in():
            raise Exception("User not logged in")
