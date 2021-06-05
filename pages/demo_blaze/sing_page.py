
class SingUpPage:

    _option_sign_id = 'signin2'
    _option_username_id = 'sign-username'
    _option_password_id = 'sign-password'
    _option_sign_up_id = '//button[contains(text(), "Sign up")]'

    def get_sign_option(self):
        return self._option_sign_id

    def get_username_option(self):
        return self._option_username_id

    def get_password_option(self):
        return self._option_password_id

    def get_sign_up_option(self):
        return self._option_sign_up_id
