import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from Utilities.handy_wrappers import HandyWrappers

class ElementPresentCheck():

    def test(self):
        baseUrl = "https://courses.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        hw = HandyWrappers(driver)
        driver.get(baseUrl)

        elementResult1 = hw.isElementPresent("//input[@name='enter-name']", By.XPATH)
        print(str(elementResult1))

        elementResult2 = hw.isElementPresent("show-hide", By.NAME)
        print(str(elementResult2))

ff = ElementPresentCheck()
ff.test()