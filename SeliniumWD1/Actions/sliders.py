from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

class Sliders():
    def test1(self):
        baseUrl = "https://jqueryui.com/slider/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        driver.switch_to.frame(0)

        element = driver.find_element(By.XPATH, "//span[@tabindex='0']")
        time.sleep(2)
        try:
            actions = ActionChains(driver)
            actions.drag_and_drop_by_offset(element, 100, 0).perform()
            print("sliding successful :-)")
            time.sleep(2)
        except:
            print("sliding unsuccessful :-(")

ff = Sliders()
ff.test1()