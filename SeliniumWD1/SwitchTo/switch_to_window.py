from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class SwitchToWindow():

    def test(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://courses.letskodeit.com/practice")
        driver.implicitly_wait(5)

        # Find parent handle -> main window
        parentHandle = driver.current_window_handle
        print("Parent handle: " + parentHandle)

        # find open win btn and click
        driver.find_element(By.XPATH, "//button[@onclick='openWindow()']").click()
        time.sleep(2)

        # find all handles, there should be two after opening new window
        handles = driver.window_handles

        # switch to window and search course
        for handle in handles:
            print("Handle: " + handle)
            if handle not in parentHandle:
                driver.switch_to.window(handle)
                print("Switched to window: " + handle)
                searchBox = driver.find_element(By.XPATH, "//input[@id='search']")
                searchBox.send_keys("python")
                time.sleep(2)
                driver.close()
                break

        # switch back to parent handle
        driver.switch_to.window(parentHandle)
        driver.find_element(By.XPATH, "//input[@placeholder='Enter Your Name']").send_keys("test success!!")


ff = SwitchToWindow()
ff.test()