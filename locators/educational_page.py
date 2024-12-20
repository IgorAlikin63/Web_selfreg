from selenium.webdriver.common.by import By
class EducationalPageLocators:

    FIRST_SLIDE_HEADER = (By.XPATH, "//h1[text()='Давайте сотрудничать!']")
    SECOND_SLIDE_HEADER = (By.XPATH, "//h1[text()='Свобода выбора']")
    THIRD_SLIDE_HEADER = (By.XPATH, "//h1[text()='Надёжный доход']")
    FOURTH_SLIDE_HEADER = (By.XPATH, "//h1[text()='Бонусы к основному доходу']")
    FIFTH_SLIDE_HEADER = (By.XPATH, "//h1[text()='Преимущества для курьеров']")
    SIXTH_SLIDE_HEADER = (By.XPATH, "//h1[text()='Чтобы начать доставки']")
    GO_ON_BUTTON = (By.XPATH, "//button[contains(@class, 'ant-btn-primary')]")