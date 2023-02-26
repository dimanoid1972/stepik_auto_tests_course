import math
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://SunInJuly.github.io/execute_script.html")

button = driver.find_element_by_tag_name("button")
driver.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

time.sleep(10)
driver.quit()