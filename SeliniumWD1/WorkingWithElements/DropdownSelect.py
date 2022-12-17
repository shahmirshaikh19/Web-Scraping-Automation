from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

class DropdownSelect():

    def test(self):
        BaseUrl = "https://courses.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(BaseUrl)
        driver.implicitly_wait(10)

        # element = driver.find_element(By.XPATH, "//select[@id='carselect']//option[@value='bmw']")

        element = driver.find_element(By.ID, "carselect")
        sel = Select(element)

        sel.select_by_value("benz")
        print("Selected Benz by value!!")
        time.sleep(2)

        sel.select_by_index("2")
        print("Selected Honda by Index!!")
        time.sleep(2)

        sel.select_by_visible_text("BMW")
        print("Selected BMW bt Visible text!!")
        time.sleep(2)

        sel.select_by_index(2)
        print("Selected Honda by Index again!!")
        time.sleep(2)

ff = DropdownSelect()
ff.test()