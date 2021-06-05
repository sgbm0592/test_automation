from selenium.webdriver.firefox.webdriver import WebDriver
from pages.demo_blaze.prod_page import ProdPage as page
from keywords.demo_blaze.base_actions import BaseActions
from selenium.webdriver.common.by import By
from assertion import assertions


class ProdActions(BaseActions):

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self._page = page()

    def verify_is_visible(self, prod):
        assertions.assert_true(self.is_visible(By.CLASS_NAME, prod),
                               'El element : {} no esta visible'.format(prod))

    def verify_prod_name(self, expected_name):
        self.verify_is_visible(self._page.get_title_option())
        assertions.assert_equal(expected_name, self.get_element(By.CLASS_NAME, self._page.get_title_option()).text,
                                'El Texto no coincide')

    def verify_prod_price(self, expected_price):
        self.verify_is_visible(self._page.get_price_option())
        assertions.assert_contains(expected_price, self.get_element(By.CLASS_NAME, self._page.get_price_option()).text,
                                'El Precio no coincide')

    def verify_add_cart_option(self):
        assertions.assert_true(self.is_visible(By.XPATH, self._page.get_add_cart()),
                               'La opcion Add to cart no esta visible')

    def click_on_prod_option(self, expected_name, expected_price):
        self.verify_prod_name(expected_name)
        self.verify_prod_price(expected_price)
        self.verify_add_cart_option()
        self.get_element(By.XPATH, self._page.get_add_cart()).click()

