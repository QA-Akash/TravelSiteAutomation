from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base.base_driver import BaseDriver


class SearchFlightResult(BaseDriver):

    # Locators
    FILTER_FLIGHT = '//p[@class="font-lightgrey bold"][normalize-space()="1"]'

    def __init__(self, driver):  # removed wait argument
        super().__init__(driver)
        self.driver = driver
        # self.wait = wait

    # Select the filter 1 Stop

    def filter_flight(self):
        # self.driver.find_element(By.XPATH, '//*[@id="flightSRP"]/section/section[2]/div/div[1]/div[2]/div[2]/label[2]/p')
        self.driver.find_element(By.XPATH, "//p[@class='font-lightgrey bold'][normalize-space()='1']")
        self.driver.implicitly_wait(10)
