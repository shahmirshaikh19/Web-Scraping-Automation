from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Screenshots():
    def test1(self):
        baseUrl = "https://courses.letskodeit.com/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(baseUrl)

        driver.find_element(By.XPATH, "//a[normalize-space()='Sign In']").click()
        driver.find_element(By.ID, "email").send_keys("abc")
        driver.find_element(By.ID, "password")
        driver.find_element(By.XPATH, "//input[@value='Login']")
        destination = "C:/Users/Dell/Desktop/test.png"

        try:
            driver.save_screenshot(destination)
            print("Screenshot Saved")
        except NotADirectoryError:
            print("Not a directory")

ff = Screenshots()
ff.test1()