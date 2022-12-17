    from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class WorkingWithElementsList():

    def test(self):
        BaseUrl = "https://courses.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(BaseUrl)
        driver.implicitly_wait(10)

        RadioBtnList = driver.find_elements(
            By.XPATH, "//input[contains(@type, 'radio') and contains(@name, 'cars')]")

        size = len(RadioBtnList)
        print("size of the list: " + str(size))

        for radioBtn in RadioBtnList:
            isSelected = radioBtn.is_selected()

            if not isSelected:
                radioBtn.click()
                time.sleep(3)

ff = WorkingWithElementsList()
ff.test()