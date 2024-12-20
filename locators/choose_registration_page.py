from selenium.webdriver.common.by import By
class ChooseRegistrationPageLocators:

    PAGE_TITLE = (By.XPATH, "//h1[text()='Выберите способ регистрации']")
    CARD_ONLINE = (By.XPATH, "//div[contains(@class, 'ChooseRegistrationPath__FlowCard')][1]")
    CARD_HUB = (By.XPATH, "//div[contains(@class, 'ChooseRegistrationPath__FlowCard')][2]")
    GO_ON_BUTTON = (By.XPATH, "//button[@class='ant-btn ant-btn-primary ant-btn-lg Button Button__vendor']//span[text()='Дальше']")
