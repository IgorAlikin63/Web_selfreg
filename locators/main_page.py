from selenium.webdriver.common.by import By
class MainPageLocators:

    PHONE_INPUT_FIELD = (By.XPATH, "//input[@class='ant-input']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@class='ant-btn ant-btn-primary ant-btn-lg Button Button__vendor PhoneCheckDesktop__phoneFormButton']")
    CAR_SWITCHER = (By.XPATH, "//div[@class='CourierSwitcher__button']//span[text()='На автомобиле']")
    PEDESTRIAN_SWITCHER = (By.XPATH, "//div[@class='CourierSwitcher__button']//span[text()='Пешком / на вело']")
