from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class SwitchToFrame():

    def test(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://courses.letskodeit.com/practice")
        driver.implicitly_wait(5)
        driver.execute_script("window.scrollBy(0,1000);")

        # switch to frame using id
        driver.switch_to.frame("courses-iframe")

        # switch to frame using name
        # driver.switch_to.frame("iframe-name")

        # switch to frame using numbers
        # driver.switch_to.frame(0)
        time.sleep(2)

        # search course
        searchBox = driver.find_element(By.XPATH, "//input[@id='search']")
        searchBox.send_keys("python")
        time.sleep(2)

        # switch back to parent frame
        driver.switch_to.default_content()
        driver.execute_script("window.scrollBy(0,-1000);")
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@placeholder='Enter Your Name']").send_keys("test success!!")
        time.sleep(2)

ff = SwitchToFrame()
ff.test()