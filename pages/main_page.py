from pages.base_page import BasePage
from urls import Urls
from locators.main_page import MainPageLocators
from data import UserData


class MainPage(BasePage):

    #открыли страницу
    def open(self):
        self.open_page(Urls.MAIN_PAGE)

    def click_in_phone_input_field(self):
        click_in_phone_input_field = self.wait_and_find_element(MainPageLocators.PHONE_INPUT_FIELD)
        self.click_element(click_in_phone_input_field)

    def send_phone_in_input(self):
        self.send_keys_in_input(MainPageLocators.PHONE_INPUT_FIELD, UserData.USER_Phone)

    def phone_submit_button_click(self):
        phone_submit_button_click = self.wait_and_find_element(MainPageLocators.SUBMIT_BUTTON)
        self.click_element(phone_submit_button_click)

