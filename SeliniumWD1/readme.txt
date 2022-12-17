-> Introduction of  the project:
In this particular project there is the basic usage of Selenium Webdriver for the web automation and basic webpage interactions.

-> OS:
Windows 10 pro

-> Browser:
Chrome browser

-> Dependancies and versions of libraries:
Chrome 108.0.5359.125
Python 3.9.7
Selenium 4.6.1
pip 21.2.3

-> What you need to do before executing the script?
-Add selenium to the project modules
-Download the chromedriver, Set the environment variable, Pass the chromedriver to the webdriver.Chrome(driverLocation)

-> Classes utilized:
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver import ActionChains
import logging
import logging.config

-> Tools Language:
PyCharm
Chrome driver
Selectors hub

-> Interacted Websites:
https://courses.letskodeit.com/practice
https://www.goibibo.com
https://jqueryui.com

-> Note: 
-Always use the same version of modules while working with webdriver
-Make sure the zoom level is 100%
-Make sure all network zones are either disabled or enabled