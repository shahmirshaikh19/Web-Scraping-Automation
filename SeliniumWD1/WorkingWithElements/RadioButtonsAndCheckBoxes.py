import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class RadioButtonsAndCheckBoxes():

    def test(self):
        BaseUrl = "https://courses.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(BaseUrl)
        driver.implicitly_wait(10)

        bmwRadio = driver.find_element(By.XPATH, "//input[@id='bmwradio']")
        bmwRadio.click()

        time.sleep(3)

        benzCheck = driver.find_element(By.XPATH, "//input[@id='benzcheck']")
        benzCheck.click()

        time.sleep(3)

        bmwCheck = driver.find_element(By.XPATH, "//input[@id='bmwcheck']")
        bmwCheck.click()

        print("BMW radiobtn is selected? " + str(bmwRadio.is_selected()))
        print("BMW checkbox is selected? " + str(bmwCheck.is_selected()))

ff = RadioButtonsAndCheckBoxes()
ff.test()