import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


@pytest.fixture(scope="class")
def setup(request):
    chrome_binary = "D:/chrome-win64/chrome-win64/chrome.exe"
    options = webdriver.ChromeOptions()
    options.binary_location = chrome_binary
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    # wait = WebDriverWait(driver, 10)
    # For the wait this is not te ideal way, so we will externalize this wevdriverWait seperately
    driver.get("https://www.yatra.com/")
    driver.maximize_window()
    request.cls.driver = driver
    # request.cls.wait = wait

    yield
    driver.close()

