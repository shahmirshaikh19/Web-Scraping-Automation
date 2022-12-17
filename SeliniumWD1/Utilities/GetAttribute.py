from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class GetAttribute():

    def test(self):
        BaseUrl = "https://courses.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(BaseUrl)
        driver.implicitly_wait(5)

        Element = driver.find_element(By.XPATH, "//input[@name='enter-name']")
        AttributeValue = Element.get_attribute("placeholder")
        print("Value of attribute is: " + AttributeValue)
        time.sleep(1)
        driver.quit()

ff = GetAttribute()
ff.test()

