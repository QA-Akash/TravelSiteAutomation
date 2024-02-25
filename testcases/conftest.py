import os.path

import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as BraveService
from webdriver_manager.core.os_manager import ChromeType


# @pytest.fixture(scope="class")
@pytest.fixture(autouse=True)
# @pytest.fixture(scope='class', autouse=True)
def setup(request, browser, url):
    if browser == "chrome":
        chrome_binary = "D:/chrome-win64/chrome-win64/chrome.exe"
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.binary_location = chrome_binary
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    elif browser == "brave":
        brave_binary = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
        options = webdriver.ChromeOptions()
        options.binary_location = brave_binary
        driver = webdriver.Chrome(service=BraveService(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()))
    else:
        print("Please provide valid browser")

    # driver.get("https://www.yatra.com/")
    driver.get(url)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--url")


@pytest.fixture(scope='class', autouse=True)  # fixture for the browser
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope='class', autouse=True)   # fixture for the url
def url(request):
    return request.config.getoption("--url")

"""
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_make_report(item, call):
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])
    if report.when == "call":
        # always add url to report
        extras.append(pytest_html.extras.url("http://www.yatra.com/"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            report_dir = os.path.dirname(item.config.option.htmlpath)
            file_name = report.nodeid.replace("::", "_") + ".png"
            destination_file = os.path.join(report_dir,file_name)
            driver.save_screenshot(destination_file)
            extras.append(pytest_html.extras.html("<div>Additional HTML</div>"))
            report.extras = extras"""



    # else:
    #     print("provide valid browser")
    # print('Login')
    # # print('Browser Product')
    # yield
    # # test_logout()
    # print("logoff")
    # print('close the browser')


"""
def pytest_addoption(parser):
        parser.addoption("--browser")

    @pytest.fixture(scope='session', autouse=True)
    def browser(request):
        return request.config.getoption("--browser")
"""

# chrome_binary = "D:/chrome-win64/chrome-win64/chrome.exe"
# options = webdriver.ChromeOptions()
# options.binary_location = chrome_binary
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
# wait = WebDriverWait(driver, 10)
# For the wait this is not te ideal way, so we will externalize this wevdriverWait seperately

# request.cls.wait = wait
