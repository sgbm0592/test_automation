
class CategoriesPage:

    _option_title_id = 'cat'
    _option_phones_xpath = '//a[contains(text(), "Phones")]'
    _option_laptops_xpath = '//a[contains(text(), "Laptops")]'
    _option_monitors_xpath = '//a[contains(text(), "Monitors")]'

    def get_title_option(self):
        return self._option_title_id

    def get_phones_option(self):
        return self._option_phones_xpath

    def get_laptops_option(self):
        return self._option_laptops_xpath

    def get_monitors_option(self):
        return self._option_monitors_xpath
