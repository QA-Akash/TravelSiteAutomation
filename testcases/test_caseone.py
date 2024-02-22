# import time
# import yaml
import pytest
import softest
from ddt import ddt, data, unpack, file_data

# from selenium import webdriver
# from selenium.webdriver import Keys
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support import expected_conditions as EC

# from Pages.search_flight_result_page import SearchFlightResult
from Pages.yatra_launch_page import LaunchPage
from utilities.utils import Utils


# Launch the travel website
# provide going to location
# Click on search flight butn
# Verify that filter result show having only one stop


@pytest.mark.usefixtures("setup")
@ddt
class Test_Search_And_verify_Filter(softest.TestCase):
    log = Utils.custom_logger()

    @pytest.fixture(autouse=True)
    def class_setup(self):  # def class_setup(self, setup)
        # self.driver = setup
        self.lp = LaunchPage(self.driver)
        self.ut = Utils()

    # @data(("Aurangabad", "Delhi", "24/02/2024", "1 Stop"))
    # @unpack

    # @file_data("../testdata/testdata.yml")
    # @data(*Utils.read_data_from_excel("D:/Cred_Rev2/TestFrameworkDemo/testdata/testdata.xlsx", "TestData"))
    @data(*Utils.read_data_from_csv("D:/Cred_Rev2/TestFrameworkDemo/testdata/test_data.csv"))
    @unpack
    def test_search_flight_1_stop(self, depart_location, arrival_location, departure_date, stops):
        """
        # Launch the travel website
        :return: travel launch page
        """
        try:
            assert 'Yatra.com' in self.driver.title
            self.log.info(self.driver.title)
            # lp = LaunchPage(self.driver)
            # search_flight_result = self.lp.search_flights('Aurangabad', 'Delhi', 24/02/2024)
            search_flight_result = self.lp.search_flights(depart_location, arrival_location, departure_date)
            self.lp.page_scroll()
            search_flight_result.filter_flight_by_stop(stops)
            # To handle the dynamic scroll
            # lp.page_scroll() # this will finally become self.lp.page_scroll()
            # Select the filter 1 stop
            # sf = SearchFlightResult(self.driver)
            # sf.filter_flight_by_stop("1 Stop")

            # print(len(sf.get_filter_flight_results()))
            # sf.click_on_specific_stop()
            # all_stops = self.wait_for_presence_of_all_elements()

            # all_stops = sf.get_search_filter_flight_results()
            all_stops = search_flight_result.get_search_filter_flight_results()
            self.log.info(len(all_stops))
            # ut = Utils()
            self.ut.assert_list_item_text(all_stops, stops)

        except:
            self.log.debug("TestCase Failed Give the correct input")
    # def test_search_flight_2_stop(self):
    #     """
    #                 # Launch the travel website
    #                 :return: travel site
    #                 """
    #     assert 'Yatra.com' in self.driver.title
    #     print(self.driver.title)
    #     # lp = LaunchPage(self.driver)
    #     search_flight_result = self.lp.search_flights('Aurangabad', 'Delhi', '27/02/2024')
    #     search_flight_result.filter_flight_by_stop("2 Stop")
    #     all_stops = search_flight_result.get_search_filter_flight_results()
    #     print(len(all_stops))
    #     self.ut.assert_list_item_text(all_stops, "2 Stops")
    #
    # def test_search_flight_non_stop(self):
    #     """
    #                 # Launch the travel website
    #                 :return: travel site
    #                 """
    #     assert 'Yatra.com' in self.driver.title
    #     print(self.driver.title)
    #     # lp = LaunchPage(self.driver)
    #     search_flight_result = self.lp.search_flights('Aurangabad', 'Delhi', '28/02/2024')
    #     search_flight_result.filter_flight_by_stop("Non Stop")
    #     all_stops = search_flight_result.get_search_filter_flight_results()
    #     print(len(all_stops))
    #     self.ut.assert_list_item_text(all_stops, "Non Stop")

    # provide from departure location
    # lp.enter_depart_from_location("Aurangabad")
    #
    # # provide goingto location
    # lp.enter_going_to_location("New Delhi")
    #
    # # select the departure date
    # lp.enter_departure_date("06/03/2024")

    # Click on the SearchFlight
    # lp.click_search_butn()

    # wait.until(EC.alert_is_present()).dismiss() wait.until(EC.presence_of_element_located((By.XPATH,
    # '//*[@id="BE_flight_origin_city"]'))) \ .send_keys("Aurangabad", Keys.ENTER) alldates = wait.until(
    # EC.element_to_be_clickable((By.XPATH, '//*[@id="BE_flight_origin_date"]'))) .find_elements(By.XPATH,
    # "//div[@id='monthWrapper']//tbody//td")
    #
    # for dates in alldates:
    #     if dates.get_attribute("date-date") == "30/12/2023":
    #         dates.click()  # Once the calendar date is click happen then calendar will disappear
    #         break
    # driver.find_element((By.XPATH, '//*[@id="BE_flight_flsearch_btn"]')).click()


""""def test_search_flight_2_stop(self):
        
# Launch the travel website
# :return: travel site

        assert 'Yatra.com' in self.driver.title
        print(self.driver.title)
        # lp = LaunchPage(self.driver)
        search_flight_result = self.lp.search_flights('Aurangabad', 'Delhi', '24/02/2024')
        search_flight_result.filter_flight_by_stop("2 Stop")
        all_stops = search_flight_result.get_search_filter_flight_results()
        print(len(all_stops))
        self.ut.assert_list_item_text(all_stops, "2 Stop")

    def test_search_flight_non_stop(self):
        
        # Launch the travel website
        # :return: travel site
        
        assert 'Yatra.com' in self.driver.title
        print(self.driver.title)
        # lp = LaunchPage(self.driver)
        search_flight_result = self.lp.search_flights('Aurangabad', 'Delhi', '24/02/2024')
        search_flight_result.filter_flight_by_stop("Non Stop")
        all_stops = search_flight_result.get_search_filter_flight_results()
        print(len(all_stops))
        self.ut.assert_list_item_text(all_stops, "Non Stop")
"""
# These details like depart_location, arrival_location, departure_date and stops will be read from Excel files in
# upcoming
