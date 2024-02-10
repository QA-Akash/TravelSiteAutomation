import time

import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC

from Pages.search_flight_result_page import SearchFlightResult
from Pages.yatra_launch_page import LaunchPage
from utilities.utils import Utils

# Launch the travel website


# provide going to location

# Click on search flight butn
# Verify that filter result show having only one stop


@pytest.mark.usefixtures("setup")
class TestDemoDropdownSingleSelect:
    def test_demoframework(self):
        """
        # Launch the travel website
        :return: travel site
        """
        assert 'Yatra.com' in self.driver.title
        print(self.driver.title)

        lp = LaunchPage(self.driver)

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
        lp.search_flights('Aurangabad', 'Delhi', '12/03/2024')
        # To handle the dynamic scroll
        lp.page_scroll()

        # Select the filter 1 stop
        sf = SearchFlightResult(self.driver)
        sf.filter_flight()

        """all_stops = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//span[contains(text(),'Non "
                                                                                   "Stop') or contains(text(),"
                                                                                   "'1 Stop') or contains(text(),"
                                                                                   "'2 Stop')]")))
        print(len(all_stops))"""

        # wait.until(EC.alert_is_present()).dismiss()
        # wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="BE_flight_origin_city"]'))) \
        #     .send_keys("Aurangabad", Keys.ENTER)
        # alldates = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="BE_flight_origin_date"]'))) .find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td")
        #
        # for dates in alldates:
        #     if dates.get_attribute("date-date") == "30/12/2023":
        #         dates.click()  # Once the calendar date is click happen then calendar will disappear
        #         break
        # driver.find_element((By.XPATH, '//*[@id="BE_flight_flsearch_btn"]')).click()
