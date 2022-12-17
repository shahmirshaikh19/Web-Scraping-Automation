from traceback import print_stack
from Utilities.handy_wrappers import HandyWrappers
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class ExplicitWaitType():

    def __init__(self, driver):
        self.driver = driver
        self.hw = HandyWrappers(driver)

    def WaitForElement(self, locator, locatorType="id",
                       timeout_1=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.hw.getByType(locatorType)
            print("Waiting for Maximum :: " + str(timeout) +
                  " :: seconds for element to be visible")
            wait = WebDriverWait(self.driver,
                                 timeout=timeout_1,
                                 poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.visibility_of_element_located((byType, locator)))
            print("Element appeared on the webpage!!")
        except:
            print("Element not appeared on the webpage!!")
        return element