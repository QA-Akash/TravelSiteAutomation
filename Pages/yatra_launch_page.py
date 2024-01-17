import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import time


class LaunchPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def departfrom(self, departlocation):
        depart_from = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="BE_flight_origin_city"]')))
        depart_from.click()
        depart_from.send_keys(departlocation)  # "New Delhi"
        depart_from.send_keys(Keys.ENTER)

    def goingto(self, goingtolocation):
        going_to = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="BE_flight_arrival_city"]')))
        going_to.click()
        self.driver.implicitly_wait(10)
        going_to.send_keys(goingtolocation)
        going_to_result = self.wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, '//*[@id="BE_flight_form_wrapper"]/div[1]/div[2]/ul/li[1]/ul/li[3]/div/div/ul/div')))
        # going_to.send_keys(Keys.ENTER)
        for city in going_to_result:
            if "New York (LGA)" in city.text:
                city.click()
                break

    def departure_date(self, departuredate):
        departdate = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="BE_flight_origin_date"]')))
        departdate.click()
        all_dates = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']"))).find_elements(
            By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")

        for date in all_dates:
            if date.get_attribute("data-date") == departuredate:
                date.click()
                break

    def click_search(self):
        self.driver.find_element(By.XPATH, '//*[@id="BE_flight_flsearch_btn"]').click()
        time.sleep(4)

