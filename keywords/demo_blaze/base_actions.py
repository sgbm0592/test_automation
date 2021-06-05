from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from factory_driver import factory_driver_wait as f_driver_w
from selenium.webdriver.support import  expected_conditions as ec
import datetime


class BaseActions:

    def __init__(self, driver: WebDriver) -> None:
        self._driver = driver

    def close_browser(self):
        self._driver.quit()

    def save_screenshot(self, filename=datetime.datetime.now().strftime('%Y%m%d_%H%M%S')):
        self._driver.save_screenshot('../screenshots/{}.png'.format(filename))

    def get_element(self, by, locator) -> WebElement:
        element = None
        try:
            element = self._driver.find_element(by, locator)
        except NoSuchElementException as nsee:
            print(nsee)
        return element

    def exist_element(self, by, locator) -> bool:
        exist = self.get_element(by, locator) != None
        return exist

    def is_visible(self, by, locator) -> bool:
        visible = False
        element = self.get_element(by, locator)
        if element != None:
            visible = element.is_displayed()
        return visible

    def is_clickable(self, by, locator, timeout) -> WebElement:
        w_driver = f_driver_w.get_driver_wait(self._driver, timeout)
        try:
            w_driver.until(ec.element_to_be_clickable((by, locator)))
            return True
        except TimeoutException:
            return False    

    def accept_alert(self):
        self._driver.switch_to.alert.accept()
