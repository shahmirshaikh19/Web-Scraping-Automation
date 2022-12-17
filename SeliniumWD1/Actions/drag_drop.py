from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

class DragDrop():
    def test1(self):
        baseUrl = "https://jqueryui.com/droppable/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        driver.switch_to.frame(0)

        fromElement = driver.find_element(By.XPATH, "//div[@id='draggable']")
        toElement = driver.find_element(By.XPATH, "//div[@id='droppable']")
        time.sleep(2)
        try:
            actions = ActionChains(driver)
            # actions.drag_and_drop(fromElement, toElement).perform()
            actions.click_and_hold(fromElement).perform()
            actions.move_to_element(toElement).perform()
            actions.release().perform()
            print("Drag and Drop element successful")
            time.sleep(2)
        except:
            print("Drag and Drop failed on element")

ff = DragDrop()
ff.test1()