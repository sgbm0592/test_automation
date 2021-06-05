from selenium.webdriver.firefox.webdriver import WebDriver
from pages.demo_blaze.main_header_page import MainHeaderPage as page
from keywords.demo_blaze.base_actions import BaseActions
from selenium.webdriver.common.by import By
from assertion import assertions


class MainHeaderActions(BaseActions):

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self._page = page()

    def verify_main_title(self):
        assertions.assert_true(self.is_visible(By.ID, self._page.get_title_id()), 'El slider no esta visible')

    def verify_text_title(self, expected_title):
        self.verify_main_title()
        assertions.assert_equal(expected_title, self.get_element(By.ID, self._page.get_title_id()).text,
                                'El Texto no coincide')