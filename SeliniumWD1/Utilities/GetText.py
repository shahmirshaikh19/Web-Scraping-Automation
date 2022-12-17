from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class GetText():

    def test(self):
        BaseUrl = "https://courses.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(BaseUrl)
        driver.implicitly_wait(5)

        OpenTabElement = driver.find_element(By.XPATH, "//a[@id='opentab']")
        element_text = OpenTabElement.text
        print("Text on element is: " + element_text)
        time.sleep(3)
        driver.quit()

ff = GetText()
ff.test()

