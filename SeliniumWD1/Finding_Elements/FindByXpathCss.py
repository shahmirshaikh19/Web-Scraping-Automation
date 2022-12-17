from selenium import webdriver
from selenium.webdriver.common.by import By

class FindByXpathCss():
    def test(self):
        baseURL = "https://courses.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        elementByXpath = driver.find_element(By.XPATH, "//input[@name='show-hide']")
        if elementByXpath is not None:
            print("Element Found -> By Xpath")


        elementByCss = driver.find_element(By.CSS_SELECTOR, "#displayed-text")
        if elementByCss is not None:
            print("Element Found -> By CSS selector")

run_tests = FindByXpathCss()
run_tests.test()