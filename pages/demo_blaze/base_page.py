from factory_driver import factory_driver
import datetime

class BasePage():

    def close_browser(self):
        self._driver.quit()

    def save_screenshot(self,filename=datetime.datetime.now().strftime('%Y%m%d_%H%M%S')):
        self._driver.save_screenshot('screenshots/{}.png'.format(filename))