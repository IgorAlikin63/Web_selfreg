from selenium.webdriver.common.by import By

class DownloadApplicationPage:

    PAGE_TITLE = (By.XPATH, "//h1[contains(@class, 'BlockHeader__title') and normalize-space(text())='Ждем вас в курьерском центре']")