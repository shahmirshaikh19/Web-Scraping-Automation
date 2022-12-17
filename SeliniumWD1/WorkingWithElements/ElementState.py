import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class ElementState():

    def isEnabled(self):
        BaseUrl = "http://www.google.com"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(BaseUrl)
        driver.implicitly_wait(10)

        e1 = driver.find_element(By.XPATH, "//input[@title='Search']")
        e1State = e1.is_enabled()
        print("E1 is Enabled? -> " + str(e1State))

        e2 = driver.find_element(By.XPATH, "//a[@class='gb_j'][@data-pid='23']")
        e2State = e2.is_enabled()
        print("E2 is Enabled? -> " + str(e2State))

        e3 = driver.find_element(By.XPATH, "//a[@class='pHiOh'][text()='About']")
        e3State = e3.is_enabled()
        print("E3 is Enabled? -> " + str(e3State))

e = ElementState()
e.isEnabled()