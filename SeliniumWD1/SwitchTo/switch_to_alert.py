from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class SwitchToAlert():

    def test1(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://courses.letskodeit.com/practice")
        driver.implicitly_wait(5)

        driver.find_element(By.XPATH, "//input[@placeholder='Enter Your Name']").send_keys("Shahmir")
        driver.find_element(By.XPATH, "//input[@id='alertbtn']").click()
        time.sleep(2)
        alert1 = driver.switch_to.alert
        alert1.accept()
        time.sleep(2)

        driver.find_element(By.XPATH, "//input[@placeholder='Enter Your Name']").send_keys("Shahmir")
        driver.find_element(By.XPATH, "//input[@id='confirmbtn']").click()
        time.sleep(2)
        alert2 = driver.switch_to.alert
        alert2.dismiss()
        time.sleep(2)

ff = SwitchToAlert()
ff.test1()