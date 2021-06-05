
class LogInPage:

    _option_login_id = 'login2'
    _option_username_id = 'loginusername'
    _option_password_id = 'loginpassword'
    _option_log_button_id = '//button[contains(text(), "Log in")]'
    _option_welcome_id = 'nameofuser'
    _option_log_out_id = 'logout2'

    def get_login_option(self):
        return self._option_login_id

    def get_logout_option(self):
        return self._option_log_out_id

    def get_username_option(self):
        return self._option_username_id

    def get_password_option(self):
        return self._option_password_id

    def get_login_button_option(self):
        return self._option_log_button_id

    def get_welcome_option(self):
        return self._option_welcome_id
