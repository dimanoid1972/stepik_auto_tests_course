import math
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://suninjuly.github.io/find_link_text")
driver.get("http://suninjuly.github.io/find_link_text_redirect13.html")
first_name = driver.find_element(By.NAME, "first_name")
first_name.send_keys("Dmitry")
last_name = driver.find_element(By.NAME, "last_name")
last_name.send_keys("Ostrowski")
city = driver.find_element(By.CLASS_NAME, "city")
city.send_keys("Kaliningrad")
country = driver.find_element(By.ID, "country")
country.send_keys("Russia")
button = driver.find_element(By.TAG_NAME, "button")
button.click()


