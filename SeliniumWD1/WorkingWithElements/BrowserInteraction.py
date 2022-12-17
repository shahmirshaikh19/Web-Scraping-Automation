import time

from selenium import webdriver
class BrowserInteractions():

    def test(self):
        baseUrl = "https://courses.letskodeit.com/practice"
        driver = webdriver.Chrome()

        # maximize browser window
        driver.maximize_window()

        # opens the given url
        driver.get(baseUrl)

        # get page title
        title = driver.title
        print("title of webpage is: " + title)
        time.sleep(3)

        # get current url of web-page
        url = driver.current_url
        print("current url of webpage is: " + url)
        time.sleep(3)

        # refresh the current page
        driver.refresh()
        print("Page refreshed 1st time")
        time.sleep(3)

        # another way to refresh the page
        driver.get(driver.current_url)
        print("Page refreshed 2nd time")
        time.sleep(3)

        # go to url
        driver.get("https://courses.letskodeit.com/login")
        print("another url opened!")
        time.sleep(3)

        # go one page back in history
        driver.back()
        print("gone one step back in browser!")
        time.sleep(3)

        # go one page forward in history
        driver.forward()
        print("gone one step forward in browser!")
        time.sleep(3)

        # open the source code of current web-page
        PageSource = driver.page_source
        print(PageSource + "that was the current page source!")
        time.sleep(3)

        # quit the browser
        driver.quit()

ff = BrowserInteractions()
ff.test()