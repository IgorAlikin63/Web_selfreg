from pages.base_page import BasePage
from locators.choose_registration_page import ChooseRegistrationPageLocators

class ChooseRegistrationPage(BasePage):

    def choose_registration_title_check(self):
        element = self.is_element_present(ChooseRegistrationPageLocators.PAGE_TITLE)
        if element and element.is_displayed():
            return True

    def check_visibility_of_hub_card(self):
        element = self.wait_and_find_element(ChooseRegistrationPageLocators.CARD_HUB)
        return element.is_displayed()

    def click_on_hub_card(self):
        click_on_hub_card = self.wait_and_find_element(ChooseRegistrationPageLocators.CARD_HUB)
        self.click_element(click_on_hub_card)

    def click_go_on_button(self):
        click_go_on_button = self.wait_and_find_element(ChooseRegistrationPageLocators.GO_ON_BUTTON)
        self.click_element(click_go_on_button)