from pages.base_page import BasePage
from locators.new_personal_page import  NewPersonalPageLocators
from data import UserData

class NewPersonalPage(BasePage):

    def click_city_input(self):
        click_city_input = self.wait_and_find_element(NewPersonalPageLocators.CITY_INPUT_FIELD)
        self.click_element(click_city_input)

    def send_moscow_in_city_input(self):
        self.send_keys_in_input(NewPersonalPageLocators.CITY_INPUT_FIELD, UserData.USER_CITY_MOSCOW)

    def click_birthday_input(self):
        click_birthday_input = self.wait_and_find_element(NewPersonalPageLocators.BIRTHDAY_INPUT_FIELD)
        self.click_element(click_birthday_input)

    def send_years_in_birthday_input(self):
        self.send_keys_in_input(NewPersonalPageLocators.BIRTHDAY_INPUT_FIELD, UserData.USER_DATE_BIRTH_VALID)

    def click_last_name_input(self):
        click_last_name_input = self.wait_and_find_element(NewPersonalPageLocators.LAST_NAME_INPUT_FIELD)
        self.click_element(click_last_name_input)

    def send_last_name_in_last_name_input(self):
        self.send_keys_in_input(NewPersonalPageLocators.LAST_NAME_INPUT_FIELD, UserData.USER_LAST_NAME_VALID)

    def click_first_name_input(self):
        click_first_name_input = self.wait_and_find_element(NewPersonalPageLocators.FIRST_NAME_INPUT_FIELD)
        self.click_element(click_first_name_input)

    def send_first_name_in_last_name_input(self):
        self.send_keys_in_input(NewPersonalPageLocators.FIRST_NAME_INPUT_FIELD, UserData.USER_FIRST_NAME_VALID)

    def click_middle_name_input(self):
        click_middle_name_input = self.wait_and_find_element(NewPersonalPageLocators.MIDDLE_NAME_INPUT_FIELD)
        self.click_element(click_middle_name_input)

    def send_middle_name_in_last_name_input(self):
        self.send_keys_in_input(NewPersonalPageLocators.MIDDLE_NAME_INPUT_FIELD, UserData.USER_MIDDLE_NAME_VALID)

    def click_email_input(self):
        click_email_input = self.wait_and_find_element(NewPersonalPageLocators.EMAIL_INPUT_FIELD)
        self.click_element(click_email_input)

    def send_email_in_email_input(self):
        self.send_keys_in_input(NewPersonalPageLocators.EMAIL_INPUT_FIELD, UserData.USER_EMAIL_VALID)

    def click_click_submit_button(self):
        click_click_submit_button = self.wait_and_find_element(NewPersonalPageLocators.SUBMIT_BUTTON)
        self.click_element(click_click_submit_button)

    def data_selector(self):
        data_selector = self.wait_and_find_element(NewPersonalPageLocators.DATE_SELECT_DEFAULT)
        self.click_element(data_selector)

    def moscow_choose_selector(self):
        moscow_choose_selector = self.wait_and_find_element(NewPersonalPageLocators.CITY_MOSCOW_IN_SELECTOR)
        self.click_element(moscow_choose_selector)

    def scroll_to_email_input(self):
        self.scroll_to_element(NewPersonalPageLocators.EMAIL_INPUT_FIELD)


