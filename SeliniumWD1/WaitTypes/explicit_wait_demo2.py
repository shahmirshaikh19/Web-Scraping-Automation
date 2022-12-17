from selenium import webdriver
from WaitTypes.explicit_wait_type import ExplicitWaitType
import time


class ExplicitWaitDemo2():

    def test(self):
        baseUrl = "https://courses.letskodeit.com/courses"
        driver = webdriver.Chrome()
        driver.implicitly_wait(2)
        driver.maximize_window()
        driver.get(baseUrl)

        wait = ExplicitWaitType(driver)
        element = wait.WaitForElement(locator="//a[@href='/login']", locatorType='xpath')

        time.sleep(2)
        driver.quit()

ff = ExplicitWaitDemo2()
ff.test()