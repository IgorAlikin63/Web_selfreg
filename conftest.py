import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from urls import Urls

@pytest.fixture
def driver(request):
    # Инициализация браузера
    browser = webdriver.Chrome(service=Service('C:/Users/alikin-igor/WebDriver/bin/yandexdriver.exe'))
    browser.maximize_window()
    browser.get(Urls.MAIN_PAGE)
    yield browser
    browser.quit()
