from selenium.webdriver.firefox.webdriver import WebDriver
from pages.demo_blaze.about_page import AboutPage as page
from keywords.demo_blaze.base_actions import BaseActions
from selenium.webdriver.common.by import By
from assertion import assertions


class AboutActions(BaseActions):

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self._page = page()

    def verify_is_visible(self, by, element):
        assertions.assert_true(self.is_visible(by, element), 'El title no esta visible')

    def verify_about_title(self):
        self.verify_is_visible(By.XPATH, self._page.get_about_option())

    def click_on_about_option(self):
        self.verify_about_title()
        self.get_element(By.XPATH, self._page.get_about_option()).click()

    def click_on_play_option(self):
        self.verify_is_visible(By.CLASS_NAME, self._page.get_play_option())
        self.get_element(By.CLASS_NAME, self._page.get_play_option()).click()

    def click_on_close_option(self):
        self.verify_is_visible(By.XPATH, self._page.get_close_option())
        self.get_element(By.XPATH, self._page.get_close_option()).click()

