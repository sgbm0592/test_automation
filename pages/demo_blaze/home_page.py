
class HomePage:

    _option_title_class = 'navbar-brand'
    _option_home_xpath = '//a[contains(text(), "Home")]'
    _option_prod_xpath = '//a[contains(text(), "{}")]'

    def get_title_option(self):
        return self._option_title_class

    def get_home_option(self):
        return self._option_home_xpath

    def get_prod_option(self, prod):
        return self._option_prod_xpath.format(prod)
