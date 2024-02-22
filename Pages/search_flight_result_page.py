import logging
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base.base_driver import BaseDriver
from utilities.utils import Utils


class SearchFlightResult(BaseDriver):
    log = Utils.custom_logger(loglevel=logging.WARNING)

    def __init__(self, driver):  # removed wait argument
        super().__init__(driver)
        self.driver = driver
        # self.wait = wait
    # Locators
    # FILTER_FLIGHT = '//p[@class="font-lightgrey bold"][normalize-space()="1"]'
    FILTER_BY_1_STOP_ICON = '//p[@class="font-lightgrey bold"][normalize-space()="1"]'
    FILTER_BY_2_STOP_ICON = '//p[@class="font-lightgrey bold"][normalize-space()="2"]'
    FILTER_BY_NON_STOP_ICON = '//p[@class="font-lightgrey bold"][normalize-space()="0"]'
    SEARCH_FLIGHT_RESULTS_LIST = "//span[contains(text(),'Non Stop') or contains(text(),'1 Stop') or contains(text(),'2 Stop')]"

    # Select the filter 1 Stop
    # def filter_flight(self):
    # self.driver.find_element(By.XPATH, '//*[@id="flightSRP"]/section/section[2]/div/div[1]/div[2]/div[2]/label[2]/p')
    # self.driver.find_element(By.XPATH, "//p[@class='font-lightgrey bold'][normalize-space()='1']")
    #     self.driver.implicitly_wait(10)
    #

    def get_filter_by_one_stop_icon(self):
        return self.driver.find_element(By.XPATH, self.FILTER_BY_1_STOP_ICON)

    def get_filter_by_two_stop_icon(self):
        return self.driver.find_element(By.XPATH, self.FILTER_BY_2_STOP_ICON)

    def get_filter_by_non_stop_icon(self):
        return self.driver.find_element(By.XPATH, self.FILTER_BY_NON_STOP_ICON)

    def filter_flight_by_stop(self, by_stop):
        if by_stop == "1 Stop":
            self.get_filter_by_one_stop_icon().click()
            self.log.warning("Selected flights with 1 stop")
            # instead of print this is used because log is at class level use self.log
            time.sleep(2)
        elif by_stop == "2 Stop":
            self.get_filter_by_one_stop_icon().click()
            self.log.warning("Selected flights with 2 stop")
            time.sleep(2)
        elif by_stop == "Non Stop":
            self.get_filter_by_one_stop_icon().click()
            self.log.debug("Selected non stop flights")
            time.sleep(2)
        else:
            self.log.critical("Please provide valid filter option")

    def get_search_filter_flight_results(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.SEARCH_FLIGHT_RESULTS_LIST)


"""
    def click_on_specific_stop(self):       
        return self.driver.find_element(By.XPATH, self.FILTER_FLIGHT).click()
"""