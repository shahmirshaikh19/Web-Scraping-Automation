from selenium import webdriver
from selenium.webdriver.common.by import By
import time

baseUrl = "https://www.goibibo.com/flights/"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(baseUrl)
driver.implicitly_wait(5)
partialText = "Del"
textToSelect = "New Dehli, India (DEL)"

textElement = driver.find_element(By.XPATH, "//div[@class='sc-gWXbKe gnEOYq']//p[@class='sc-giYglK eCwiKJ fswWidgetPlaceholder'][normalize-space()='Enter city or airport']").click()
textInput = driver.find_element(By.XPATH, "//input[@type='text']")
textInput.send_keys(partialText)
time.sleep(2)

ulElement = driver.find_element(By.XPATH, "//ul[@id='autoSuggest-list']")
liTags = ulElement.get_attribute("role")
print(liTags)