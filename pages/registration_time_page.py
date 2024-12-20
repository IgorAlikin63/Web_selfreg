from pages.base_page import BasePage
from locators.registration_time_page import RegistrationTimePageLocators

class RegistrationTimePage(BasePage):

    def registration_time_title_check(self):
        element = self.is_element_present(RegistrationTimePageLocators.PAGE_TITLE)
        if element and element.is_displayed():
            return True

    def click_sign_in_button(self):
        click_sign_in_button = self.wait_and_find_element(RegistrationTimePageLocators.SIGN_IN_BUTTON)
        self.click_element(click_sign_in_button)