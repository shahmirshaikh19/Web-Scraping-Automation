from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ClickAndSendKeys():

    def test(self):
        BaseUrl = "https://courses.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(BaseUrl)
        driver.implicitly_wait(10)

        LoginLink = driver.find_element(By.XPATH, "//a[@href='/login']")
        LoginLink.click()
        time.sleep(3)
        EmailField = driver.find_element(By.XPATH, "//input[@placeholder='Email Address']")
        EmailField.send_keys("TESTING!!")
        time.sleep(3)
        PasswordField = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
        PasswordField.send_keys("testing!!!")
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@placeholder='Email Address']").clear()
        time.sleep(3)
        EmailField.send_keys("test")
        time.sleep(3)
ff = ClickAndSendKeys()
ff.test()