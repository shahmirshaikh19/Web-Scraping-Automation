from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ImplicitWaitDemo():
    def test(self):
        baseUrl = "https://courses.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        loginLink = driver.find_element(By.XPATH, "//a[normalize-space()='Sign In']")
        loginLink.click()

        emailField = driver.find_element(By.XPATH, "//input[@tabindex='4']")
        emailField.send_keys("Testing")

ff = ImplicitWaitDemo()
ff.test()