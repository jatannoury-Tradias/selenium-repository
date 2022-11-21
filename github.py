from selenium import webdriver
import chromedriver_autoinstaller
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

driver = webdriver.Chrome()
driver.get("https://github.com/login")
username=driver.find_element(By.ID,"login_field")
username.send_keys("jatannoury-Tradias")

password=driver.find_element(By.ID,"password")
password.send_keys("22Q1D99z*")


login_button=driver.find_element(By.NAME,"commit")
driver.implicitly_wait(5)
login_button.click()

time.sleep(10)