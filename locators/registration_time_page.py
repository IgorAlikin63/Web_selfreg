from selenium.webdriver.common.by import By
class RegistrationTimePageLocators:

    PAGE_TITLE = (By.XPATH, "//h1[text()='Активация в курьерском центре']")
    SIGN_IN_BUTTON = (By.XPATH, "//button[@class='ant-btn ant-btn-primary ant-btn-lg Button Button__vendor RegistrationTime__button']//span[text()='Записаться']")