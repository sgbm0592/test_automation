from pages.demo_blaze.base_page import BasePage
from factory_driver import factory_driver

class ElementsOptionsPage(BasePage):

    _option_textbox_xpath = '//span[text() = "Text Box"]'


    def verify_textbox_option(self):
        return self._driver.find_element_by_xpath(self._option_textbox_xpath).is_displayed()

    def click_on_elements_option(self):
        self._driver.find_element_by_xpath(self._option_textbox_xpath).click()