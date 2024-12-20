from pages.base_page import BasePage
from locators.download_application import DownloadApplicationPage

class DownloadApplication(BasePage):

    def check_download_application_page_title(self):
        element = self.is_element_present(DownloadApplicationPage.PAGE_TITLE)
        if element and element.is_displayed():
            return True

    def check_current_url(self):
        current_url = self.get_url()
        return current_url
