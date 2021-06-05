from selenium.webdriver.firefox.webdriver import WebDriver
from pages.demo_blaze.categories_page import CategoriesPage as page
from keywords.demo_blaze.base_actions import BaseActions
from selenium.webdriver.common.by import By
from assertion import assertions


class CategoriesActions(BaseActions):

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self._page = page()

    def verify_text_title(self, by, element):
        assertions.assert_true(self.is_visible(by, element), 'El title no esta visible')

    def verify_cat_title(self):
        self.verify_text_title(By.ID, self._page.get_title_option())

    def verify_cat_options(self):
        self.verify_text_title(By.ID, self._page.get_title_option())

    def click_on_phones_option(self):
        self.verify_text_title(By.XPATH, self._page.get_phones_option())
        self.get_element(By.XPATH, self._page.get_phones_option()).click()

    def click_on_laptops_option(self):
        self.verify_text_title(By.XPATH, self._page.get_laptops_option())
        self.get_element(By.XPATH, self._page.get_laptops_option()).click()

    def click_on_monitors_option(self):
        self.verify_text_title(By.XPATH, self._page.get_monitors_option())
        self.get_element(By.XPATH, self._page.get_monitors_option()).click()
