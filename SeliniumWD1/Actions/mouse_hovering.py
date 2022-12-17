from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

class MouseHovering():

    def test1(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://courses.letskodeit.com/practice")
        driver.implicitly_wait(5)

        driver.execute_script("window.scrollBy(0, 600);")
        time.sleep(2)
        element = driver.find_element(By.ID, "mousehover")
        itemToClickLocator = ".//div[@class='mouse-hover-content']//a[text()='Top']"

        try:
            actions = ActionChains(driver)
            actions.move_to_element(element).perform()
            print("Mouse Hovered on element")
            time.sleep(2)
            topLink = driver.find_element(By.XPATH, itemToClickLocator)
            actions.move_to_element(topLink).click().perform()
            print("Item Clicked")
        except:
            print("mouse hover failed on element")

ff = MouseHovering()
ff.test1()