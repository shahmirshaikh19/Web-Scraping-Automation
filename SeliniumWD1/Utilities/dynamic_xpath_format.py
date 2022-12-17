from selenium import webdriver
from selenium.webdriver.common.by import By
from Utilities.handy_wrappers import HandyWrappers
import time


class DynamicXPathFormat():

    def test(self):
        baseUrl = "https://courses.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseUrl)

        # Login -> Lecture "How to click and type on a web element"
        driver.find_element(By.XPATH, "//a[@href='/login']").click()
        email = driver.find_element(By.XPATH, "//input[@tabindex='4']")
        email.send_keys("test@email.com")
        password = driver.find_element(By.XPATH, "//input[@tabindex='5']")
        password.send_keys("abcabc")
        driver.find_element(By.XPATH, "//input[@tabindex='7']").click()

        # Search for courses -> You don't need to search the course
        # You can select it without searching also
        courses = driver.find_element(By.XPATH, "//li[@data-id='41189']/a[@href='/courses']")
        courses.click()
        searchBox = driver.find_element(By.XPATH, "//input[@id='search']")
        searchBox.send_keys("JavaScript")
        driver.find_element(By.XPATH, "//button[@class='find-course search-course']").click()

        # Select Course
        _course = "//div[@class='zen-course-title dynamic-text']/h4[contains(text(),'{0}')]"
        _courseLocator = _course.format("JavaScript for beginners")

        courseElement = driver.find_element(By.XPATH, _courseLocator)
        courseElement.click()


ff = DynamicXPathFormat()
ff.test()