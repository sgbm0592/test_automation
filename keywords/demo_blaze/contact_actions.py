from selenium.webdriver.firefox.webdriver import WebDriver
from pages.demo_blaze.contact_page import ContactPage as page
from keywords.demo_blaze.base_actions import BaseActions
from selenium.webdriver.common.by import By
from assertion import assertions


class ContactActions(BaseActions):

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self._page = page()

    def verify_is_visible(self, by, prod):
        assertions.assert_true(self.is_visible(by, prod),
                               'El element : {} no esta visible'.format(prod))

    def verify_contact_title(self, expected_name):
        self.verify_is_visible(By.XPATH, self._page.get_contact_option())
        assertions.assert_equal(expected_name, self.get_element(By.XPATH, self._page.get_contact_option()).text,
                                'El Texto no coincide')

    def click_contact_option(self, expected_name):
        self.verify_contact_title(expected_name)
        self.get_element(By.XPATH, self._page.get_contact_option()).click()

    def send_email_option(self, email):
        self.verify_is_visible(By.ID, self._page.get_email_option())
        element = self.get_element(By.ID, self._page.get_email_option())
        assertions.assert_true(element.is_enabled(), 'El email no esta activado')
        element.send_keys(email)
        #assertions.assert_contains(name, element.text, 'El email no coincide')
        assertions.assert_true(element.is_displayed(), 'El email no esta visible')

    def send_name_option(self, name):
        self.verify_is_visible(By.ID, self._page.get_name_option())
        element = self.get_element(By.ID, self._page.get_name_option())
        assertions.assert_true(element.is_enabled(), 'El Name no esta activado')
        element.send_keys(name)
        #assertions.assert_contains(name, element.text, 'El Name no coincide')
        assertions.assert_true(element.is_displayed(), 'El Name no esta visible')

    def send_message_option(self, message):
        self.verify_is_visible(By.ID, self._page.get_message_option())
        element = self.get_element(By.ID, self._page.get_message_option())
        assertions.assert_true(element.is_enabled(), 'El message no esta activado')
        element.send_keys(message)
        #assertions.assert_contains(name, element.text, 'El message no coincide')
        assertions.assert_true(element.is_displayed(), 'El message no esta visible')

    def click_send_option(self):
        self.verify_is_visible(By.XPATH, self._page.get_send_option())
        self.get_element(By.XPATH, self._page.get_send_option()).click()

    def fill_contact_form(self, email, name, message):
        self.send_email_option(email)
        self.send_name_option(name)
        self.send_message_option(message)
        self.click_send_option()
        self.accept_alert()