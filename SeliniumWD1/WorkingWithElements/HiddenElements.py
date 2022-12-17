from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class HiddenElements():

    def letskodeit(self):
        BaseUrl = "https://courses.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(BaseUrl)
        driver.implicitly_wait(5)

        # Find the state of textbox
        TextboxElement = driver.find_element(By.XPATH, "//input[@id='displayed-text']")
        TextboxState = TextboxElement.is_displayed()
        print("text box available? " + str(TextboxState))
        time.sleep(2)

        # Click the hide btn
        driver.find_element(By.XPATH, "//input[@id='hide-textbox']").click()
        time.sleep(2)

        # Find the state of textbox again
        TextboxElement = driver.find_element(By.XPATH, "//input[@id='displayed-text']")
        TextboxState = TextboxElement.is_displayed()
        print("text box available? " + str(TextboxState))
        time.sleep(2)

        # Click the show btn
        driver.find_element(By.XPATH, "//input[@id='show-textbox']").click()
        time.sleep(2)

        # Find the state of textbox again
        TextboxElement = driver.find_element(By.XPATH, "//input[@id='displayed-text']")
        TextboxState = TextboxElement.is_displayed()
        print("text box available? " + str(TextboxState))
        time.sleep(2)

        driver.quit()

ff = HiddenElements()
ff.letskodeit()