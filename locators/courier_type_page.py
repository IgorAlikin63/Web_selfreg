from selenium.webdriver.common.by import By
class CourierTypePageLocators:

    PAGE_TITLE = (By.XPATH, "//h1[text()='Как будете доставлять заказ?']")
    VEHICLE_CARD = (By.XPATH, "//label[contains(@class, 'ant-radio-wrapper')][1]")
    BIKE_CARD = (By.XPATH, "//label[contains(@class, 'ant-radio-wrapper')][2]")
    PEDESTRIAN_CARD = (By.XPATH, "//label[contains(@class, 'ant-radio-wrapper')][3]")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(@class, 'ant-btn-primary') and .//span[text()='Дальше']]")

