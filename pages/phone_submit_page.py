from pages.base_page import BasePage
from locators.phone_submit_page import PhoneSubmitPageLocators
from data import UserData


class PhoneSubmitPage(BasePage):
    def click_in_sms_code_input_field(self):
        click_in_sms_code_input_field = self.wait_and_find_element(PhoneSubmitPageLocators.SMS_CODE_INPUT_FIELD)
        self.click_element(click_in_sms_code_input_field)

    def send_sms_code_in_input(self):
        self.send_keys_in_input(PhoneSubmitPageLocators.SMS_CODE_INPUT_FIELD, UserData.USER_SMS_CODE_DEFAULT)