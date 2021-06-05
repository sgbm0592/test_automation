
class ProdPage:

    _option_title_class = 'name'
    _option_price_class = 'price-container'
    _option_add_to_cart = '//a[contains(text(), "Add to cart")]'

    def get_title_option(self):
        return self._option_title_class

    def get_price_option(self):
        return self._option_price_class

    def get_add_cart(self):
        return self._option_add_to_cart
