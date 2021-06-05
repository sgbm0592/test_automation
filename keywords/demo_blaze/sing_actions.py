from selenium.webdriver.firefox.webdriver import WebDriver
from pages.demo_blaze.sing_page import SingUpPage as page
from keywords.demo_blaze.base_actions import BaseActions
from selenium.webdriver.common.by import By
from assertion import assertions


class SingUpActions(BaseActions):

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self._page = page()

    def verify_is_visible(self, by, element):
        assertions.assert_true(self.is_visible(by, element), 'El title no esta visible')

    def verify_sign_title(self):
        self.verify_is_visible(By.ID, self._page.get_sign_option())

    def click_on_sign_option(self):
        self.verify_sign_title()
        self.get_element(By.ID, self._page.get_sign_option()).click()



    def send_username_option(self, username):
        self.verify_is_visible(By.ID, self._page.get_username_option())
        element = self.get_element(By.ID, self._page.get_username_option())
        assertions.assert_true(element.is_enabled(), 'El Username no esta activado')
        element.send_keys(username)
        # assertions.assert_contains(name, element.text, 'El Username no coincide')
        assertions.assert_true(element.is_displayed(), 'El Username no esta visible')

    def send_password_option(self, name):
        self.verify_is_visible(By.ID, self._page.get_password_option())
        element = self.get_element(By.ID, self._page.get_password_option())
        assertions.assert_true(element.is_enabled(), 'El Password no esta activado')
        element.send_keys(name)
        # assertions.assert_contains(name, element.text, 'El Password no coincide')
        assertions.assert_true(element.is_displayed(), 'El Password no esta visible')

    def click_sign_option(self):
        self.verify_is_visible(By.XPATH, self._page.get_sign_up_option())
        self.get_element(By.XPATH, self._page.get_sign_up_option()).click()

    def fill_sign_form(self, username, password):
        self.send_username_option(username)
        self.send_password_option(password)
        self.click_sign_option()
        #self.accept_alert()
