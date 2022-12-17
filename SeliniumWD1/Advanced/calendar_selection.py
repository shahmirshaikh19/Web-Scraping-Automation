from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class CalendarSelection():

    def test1(self):
        baseUrl = "https://www.expedia.com/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        # Click flights tab
        flights = driver.find_element(By.XPATH, "//a[@class='uitk-tab-anchor']//span[text()= 'Flights']")
        flights.click()

        # find departing field
        departingField = driver.find_element(By.XPATH, "//button[@id='d1-btn']")

        # click departing field
        departingField.click()

        # find date to be selected
        dateSet = driver.find_element(By.XPATH, "//button[@aria-label='Dec 30, 2022']")

        # click the date
        dateSet.click()

        time.sleep(3)
        driver.quit()

    def test2(self):
        baseUrl = "https://www.goibibo.com/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        # Click flights tab
        flights = driver.find_element(By.XPATH, "//a[@class='nav-link active']")
        flights.click()

        # click departing field
        departingField = driver.find_element(By.XPATH, "//span[normalize-space()='Departure']")
        departingField.click()

        calMonth = driver.find_element(By.XPATH, "//*[@id='root']/div[3]/div/div/div[1]/div[3]/div[2]/div[2]/div/div/div[2]/div[1]")
        allValidDates = calMonth.find_elements(By.XPATH, "//div[@aria-disabled='false']")

        time.sleep(2)

        for date in allValidDates:
            if date.text == "31":
                date.click()
                break

ff = CalendarSelection()
ff.test2()