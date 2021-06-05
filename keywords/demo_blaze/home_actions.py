from selenium.webdriver.firefox.webdriver import WebDriver
from pages.demo_blaze.home_page import HomePage as page
from keywords.demo_blaze.base_actions import BaseActions
from selenium.webdriver.common.by import By
from assertion import assertions


class HomeActions(BaseActions):

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self._page = page()

    def verify_title_option(self):
        assertions.assert_true(self.is_visible(By.CLASS_NAME, self._page.get_title_option()),
                               'La opcion Elements no esta visible')

    def click_on_home_option(self):
        self.verify_title_option()
        self.verify_title_clickable()
        self.get_element(By.XPATH, self._page.get_home_option()).click()

    def verify_title_clickable(self):
        assertions.assert_true(self.is_clickable(By.CLASS_NAME, self._page.get_title_option(), 5),
                               'El elemento no es clickable')

    def verify_prod_clickable(self, prod):
        assertions.assert_true(self.is_clickable(By.XPATH, self._page.get_prod_option(prod), 5),
                               'El elemento no es clickable')

    def click_prod_option(self, prod):
        self.verify_prod_clickable(prod)
        self.get_element(By.XPATH, self._page.get_prod_option(prod)).click()
