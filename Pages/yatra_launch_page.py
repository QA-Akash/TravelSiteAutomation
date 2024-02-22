import logging
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from Pages.search_flight_result_page import SearchFlightResult
from base.base_driver import BaseDriver
from utilities.utils import Utils


class LaunchPage(BaseDriver):
    log = Utils.custom_logger()

    def __init__(self, driver):  # wait is removed
        super().__init__(driver)
        self.driver = driver
        # self.wait = wait  # wait is commented

    # Locators
    DEPART_FROM__FIELD = '//*[@id="BE_flight_origin_city"]'
    GOING_TO_FIELD = '//*[@id="BE_flight_arrival_city"]'
    GOING_TO_RESULT_LIST = '//div[@class="viewport"]//div[1]/li'
    SELECT_DATE_FIELD = 'BE_flight_origin_date'
    ALL_DATES = '//div[@id="monthWrapper"]//tbody//td[@class!="inActiveTD"]'
    SEARCH_BTN = '//*[@id="BE_flight_flsearch_btn"]'

    def get_depart_from_field(self):
        """
        :return: returns locator for the departure from field
        """
        return self.wait_until_element_clickable(By.XPATH, self.DEPART_FROM__FIELD)

    def get_going_to_location(self):
        """
        :return: returns locators for the going to field
        """
        return self.wait_until_element_clickable(By.XPATH, self.GOING_TO_FIELD)

    def get_going_to_result(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.GOING_TO_RESULT_LIST)

    def get_departure_date_field(self):
        return self.wait_until_element_clickable(By.ID, self.SELECT_DATE_FIELD).click()

    def get_all_dates_field(self):
        return self.wait_until_element_clickable(By.XPATH, self.ALL_DATES)

    def get_search_button(self):
        return self.driver.find_element(By.XPATH, self.SEARCH_BTN)

    def enter_depart_from_location(self, depart_location):
        """
        :return: to actions on that field
        """
        self.get_depart_from_field().click()
        self.get_depart_from_field().send_keys(
            depart_location)  # we don't get auto-suggestion because we have wrapped the methods now
        self.get_depart_from_field().send_keys(Keys.ENTER)

    # Action we are going to perform on the web-element
    def enter_going_to_location(self, arrival_location):
        self.get_going_to_location().click()
        self.log.info("Clicked on Going To")
        self.get_going_to_location().send_keys(arrival_location)
        self.log.info("Typed going to the field successfully")
        # self.get_going_to_location
        # n().send_keys(Keys.ENTER)

        search_results = self.get_going_to_result()
        # going_to.send_keys(Keys.ENTER)
        for city in search_results:
            if arrival_location in city.text:
                city.click()
                break

    def enter_departure_date(self, departuredate):
        # self.wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="BE_flight_origin_date"]'))).click()
        self.get_departure_date_field()
        # all_dates = self.wait.until(
        #     EC.element_to_be_clickable(
        #         (By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']"))).find_elements(By.XPATH,
        #                                                                                                  "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")
        all_dates = self.get_all_dates_field().find_elements(By.XPATH, self.ALL_DATES)
        # all_dates.find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")

        for date in all_dates:
            if date.get_attribute("data-date") == departuredate:
                date.click()
                break

    def click_search_butn(self):
        self.driver.find_element(By.XPATH, '//*[@id="BE_flight_flsearch_btn"]').click()
        time.sleep(4)

    def search_flights(self, depart_location, arrival_location, departure_date):
        self.enter_depart_from_location(depart_location)
        self.enter_going_to_location(arrival_location)
        self.enter_departure_date(departure_date)
        self.click_search_butn()
        search_fight_result = SearchFlightResult(self.driver)
        return search_fight_result


"""
    def depart_from(self, departlocation):
        # depart_from = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="BE_flight_origin_city"]')))
        depart_from = self.wait_until_element_clickable(self.DEPART_FROM__FIELD)
        depart_from.click()
        depart_from.send_keys(departlocation)  # "New Delhi"
        depart_from.send_keys(Keys.ENTER)
"""

"""    def goingto(self, goingtolocation):
        # going_to = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="BE_flight_arrival_city"]')))
        going_to = self.wait_until_element_clickable(By.XPATH, )
        going_to.click()
        going_to.send_keys(goingtolocation)
"""
# self.driver.implicitly_wait(10)
# going_to_result = self.wait.until(EC.presence_of_all_elements_located(
#     (By.XPATH, '//*[@id="BE_flight_form_wrapper"]/div[1]/div[2]/ul/li[1]/ul/li[3]/div/div/ul/div')))


# To handle dynamic Scroll
# this has been given and  modified to baseDriver from base package
