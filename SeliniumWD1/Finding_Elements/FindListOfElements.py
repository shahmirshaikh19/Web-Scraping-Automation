from selenium import webdriver
from selenium.webdriver.common.by import By

class FindListOfElements():
    def test(self):
        baseURL = "https://courses.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        elementListByClass = driver.find_elements(By.CLASS_NAME, "inputs")
        length1 = len(elementListByClass)

        if elementListByClass is not None:
            print("Class Name -> Size of the list is: " + str(length1))

        elementListByTagName = driver.find_elements(By.TAG_NAME, "td")
        length2 = len(elementListByTagName)

        if elementListByTagName is not None:
            print("Tag Name -> Size of the list is: " + str(length2))

run_test = FindListOfElements()
run_test.test()