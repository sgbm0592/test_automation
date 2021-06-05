
class AboutPage:

    _option_about_xpath = '//a[contains(text(), "About us")]'
    _option_play_class = 'vjs-big-play-button'
    _option_close_xpath = '//button[contains(text(), "Close")]'

    def get_about_option(self):
        return self._option_about_xpath

    def get_play_option(self):
        return self._option_play_class

    def get_close_option(self):
        return self._option_close_xpath