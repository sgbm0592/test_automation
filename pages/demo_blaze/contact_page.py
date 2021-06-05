
class ContactPage:

    _option_contact_xpath = '//a[contains(text(), "Contact")]'
    _option_send_xpath = '//button[contains(text(), "Send message")]'
    _option_email_id = 'recipient-email'
    _option_name_id = 'recipient-name'
    _option_message_id = 'message-text'

    def get_contact_option(self):
        return self._option_contact_xpath

    def get_send_option(self):
        return self._option_send_xpath

    def get_email_option(self):
        return self._option_email_id

    def get_name_option(self):
        return self._option_name_id

    def get_message_option(self):
        return self._option_message_id
