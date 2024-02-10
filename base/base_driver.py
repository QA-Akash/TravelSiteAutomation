from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseDriver:
    """
    Base driver class which will wrap or which will have common methods that can be reused by any of pages or any of the
    pages that are there in the application so all the pages we will simply inherit this particular base driver
    """

    def __init__(self, driver):
        self.driver = driver

    def page_scroll(self):
        pageLength = self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);var "
                                                "pageLength=document.body.scrollHeight;return pageLength;")
        match = False
        while match == False:
            lastcount = pageLength
            self.driver.implicitly_wait(10)
            pageLength = self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);var "
                                                    "pageLength=document.body.scrollHeight;return pageLength;")
            # ); return document.body.scrollHeight
            if lastcount == pageLength:
                match = True

    def wait_for_presence_of_all_elements(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        list_of_elements = wait.until(EC.presence_of_all_elements_located((locator_type, locator)))

        return list_of_elements

    def wait_until_element_clickable(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        return element

# print(len(list_of_elements))


# By.XPATH, "//span[contains(text(),'Non "
#                                                                                    "Stop') or contains(text(),"
#                                                                                    "'1 Stop') or contains(text(),"
#                                                                                    "'2 Stop')]"
