from selenium.webdriver.common.by import By
class NewPersonalPageLocators:

    PAGE_TITLE = (By.XPATH, "//h1[text()='Расскажите о себе']")
    CITY_INPUT_FIELD = (By.XPATH, "//input[@id='city']")
    CITY_MOSCOW_INPUT_FIELD = (By.XPATH, "//span[@class='ant-select-selection-item' and @title='Москва']")
    CITY_MOSCOW_IN_SELECTOR = (By.XPATH, "//div[contains(@class, 'ant-select-item-option-content') and text()='Москва']")
    CITIZENSHIP_INPUT_FIELD = (By.XPATH, "//input[@id='citizenship']")
    RUSSIA_CITIZENSHIP_IN_SELECTOR = (By.XPATH, "// div[text() = 'Российская Федерация']")
    BIRTHDAY_INPUT_FIELD = (By.XPATH, "//input[@placeholder='Дата рождения']")
    LAST_NAME_INPUT_FIELD = (By.XPATH, "//input[@placeholder='Фамилия']")
    FIRST_NAME_INPUT_FIELD = (By.XPATH, "//input[@placeholder='Имя']")
    MIDDLE_NAME_INPUT_FIELD = (By.XPATH, "//input[@placeholder='Отчество']")
    EMAIL_INPUT_FIELD = (By.XPATH, "//input[@placeholder='E-mail']")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(@class, 'ant-btn-primary') and .//span[text()='Дальше']]")
    DATE_SELECT_DEFAULT = (By.XPATH, "//div[contains(@class, 'ant-picker-cell-inner') and text()='1']")
