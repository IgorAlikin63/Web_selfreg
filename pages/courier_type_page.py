from pages.base_page import BasePage
from locators.courier_type_page import CourierTypePageLocators

class CourierTypePage(BasePage):

    def click_bike_icon(self):
        click_bike_icon = self.wait_and_find_element(CourierTypePageLocators.BIKE_CARD)
        self.click_element(click_bike_icon)

    def click_submit_button(self):
        click_submit_button = self.wait_and_find_element(CourierTypePageLocators.SUBMIT_BUTTON)
        self.click_element(click_submit_button)