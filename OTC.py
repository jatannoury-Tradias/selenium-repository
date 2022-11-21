from selenium import webdriver
import chromedriver_autoinstaller
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

driver = webdriver.Chrome()
driver.get("https://uat.tradias.link/")
username=driver.find_element(By.NAME,"email")
username.send_keys("j.tannoury.ext@bankhaus-scheich.de")

password=driver.find_element(By.NAME,"password")
password.send_keys("veP7gPnojxk!5")


login_button=password=driver.find_element(By.XPATH,"//*[@id='__next']/div[1]/div/div/div[2]/div[2]/div/div[2]/div/button")
driver.implicitly_wait(5)
login_button.click()

time.sleep(10)