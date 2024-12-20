from pages.main_page import MainPage
from pages.choose_registration_page import ChooseRegistrationPage
from pages.courier_type_page import CourierTypePage
from pages.educational_page import EducationalPage
from pages.new_personal_page import NewPersonalPage
from pages.phone_submit_page import PhoneSubmitPage
from pages.registration_time_page import RegistrationTimePage
from pages.download_application import DownloadApplication
from urls import Urls

class TestMainPage:

    def test_courier_registration_rus_moscow(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_in_phone_input_field()
        main_page.send_phone_in_input()
        main_page.phone_submit_button_click()
        phone_submit_page = PhoneSubmitPage(driver)
        phone_submit_page.send_sms_code_in_input()
        new_personal_page = NewPersonalPage(driver)
        new_personal_page.click_city_input()
        new_personal_page.send_moscow_in_city_input()
        new_personal_page.moscow_choose_selector()
        new_personal_page.click_first_name_input()
        new_personal_page.send_first_name_in_last_name_input()
        new_personal_page.click_last_name_input()
        new_personal_page.send_last_name_in_last_name_input()
        new_personal_page.click_middle_name_input()
        new_personal_page.send_middle_name_in_last_name_input()
        new_personal_page.click_birthday_input()
        new_personal_page.send_years_in_birthday_input()
        new_personal_page.data_selector()
        new_personal_page.scroll_to_email_input()
        new_personal_page.click_email_input()
        new_personal_page.send_email_in_email_input()
        new_personal_page.click_click_submit_button()
        courier_type_page = CourierTypePage(driver)
        courier_type_page.click_bike_icon()
        courier_type_page.click_submit_button()
        educational_page = EducationalPage(driver)
        educational_page.first_slide_check()
        educational_page.scroll_to_go_on_button()
        educational_page.click_go_on_button()
        educational_page.second_slide_check()
        educational_page.scroll_to_go_on_button()
        educational_page.click_go_on_button()
        educational_page.third_slide_check()
        educational_page.scroll_to_go_on_button()
        educational_page.click_go_on_button()
        educational_page.fourth_slide_check()
        educational_page.scroll_to_go_on_button()
        educational_page.click_go_on_button()
        educational_page.fifth_slide_check()
        educational_page.scroll_to_go_on_button()
        educational_page.click_go_on_button()
        educational_page.sixth_slide_check()
        educational_page.scroll_to_go_on_button()
        educational_page.click_go_on_button()
        choose_registration_page = ChooseRegistrationPage(driver)
        choose_registration_page.check_visibility_of_hub_card()
        choose_registration_page.click_on_hub_card()
        choose_registration_page.click_go_on_button()
        registration_time_page = RegistrationTimePage(driver)
        registration_time_page.click_sign_in_button()
        download_application_page = DownloadApplication(driver)
        download_application_page.check_download_application_page_title()
        current_url = download_application_page.check_current_url()
        assert current_url == Urls.DOWNLOAD_APPLICATION_PAGE
