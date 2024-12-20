from pages.base_page import BasePage
from locators.educational_page import EducationalPageLocators

class EducationalPage(BasePage):

    def first_slide_check(self):
        element = self.is_element_present(EducationalPageLocators.FIRST_SLIDE_HEADER)
        if element and element.is_displayed():
            return True

    def second_slide_check(self):
        element = self.is_element_present(EducationalPageLocators.SECOND_SLIDE_HEADER)
        if element and element.is_displayed():
            return True

    def third_slide_check(self):
        element = self.is_element_present(EducationalPageLocators.THIRD_SLIDE_HEADER)
        if element and element.is_displayed():
            return True

    def fourth_slide_check(self):
        element = self.is_element_present(EducationalPageLocators.FOURTH_SLIDE_HEADER)
        if element and element.is_displayed():
            return True

    def fifth_slide_check(self):
        element = self.is_element_present(EducationalPageLocators.FIFTH_SLIDE_HEADER)
        if element and element.is_displayed():
            return True

    def sixth_slide_check(self):
        element = self.is_element_present(EducationalPageLocators.SIXTH_SLIDE_HEADER)
        if element and element.is_displayed():
            return True

    def click_go_on_button(self):
        click_go_on_button = self.wait_and_find_element(EducationalPageLocators.GO_ON_BUTTON)
        self.click_element(click_go_on_button)

    def scroll_to_go_on_button(self):
        self.scroll_to_element(EducationalPageLocators.GO_ON_BUTTON)