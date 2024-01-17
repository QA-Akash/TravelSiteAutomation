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

from Pages.yatra_launch_page import LaunchPage


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
        time.sleep(4)

        lp = LaunchPage(self.driver, self.wait)

        # provide from departure location
        lp.departfrom("New Delhi")

        # provide goingto location
        lp.goingto("New York")

        # select the departure date
        lp.departure_date("26/01/2024")

        # Click on the SearchFlight
        lp.click_search()

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
