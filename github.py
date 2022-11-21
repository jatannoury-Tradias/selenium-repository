from selenium import webdriver
import chromedriver_autoinstaller
import time
from selenium.webdriver.common.by import By
import pyperclip
import os
from selenium.webdriver.common.keys import Keys
import shutil
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

# driver.implicitly_wait(5)
show_more=driver.find_element(By.LINK_TEXT,"jatannoury-Tradias/selenium-repository")
show_more.click()
driver.implicitly_wait(5)

otc=driver.find_element(By.XPATH,"/html/body/div[5]/div/main/turbo-frame/div/div/div/div[3]/div[1]/div[3]/div[3]/div[1]/div[3]/div[2]/span/a")
otc.click()
driver.implicitly_wait(5)
time.sleep(2)
driver.get("https://github.com/jatannoury-Tradias/selenium-repository")

github=driver.find_element(By.XPATH,"/html/body/div[5]/div/main/turbo-frame/div/div/div/div[3]/div[1]/div[3]/div[3]/div[1]/div[4]/div[2]/span/a")
github.click()
driver.implicitly_wait(5)
time.sleep(2)
driver.get("https://github.com/jatannoury-Tradias/selenium-repository")

time.sleep(2)
driver.get("https://github.com/")

github=driver.find_element(By.XPATH,"/html/body/div[5]/div/aside/div/loading-context/div/div[1]/div/h2/a")
github.click()
driver.implicitly_wait(5)
time.sleep(2)

repo_name=driver.find_element(By.XPATH,"/html/body/div[5]/main/div/form/div[2]/auto-check/dl/dd/input")
repo_name.send_keys("selenium-repository")
time.sleep(2)
repo_name.clear()
repo_name.send_keys("new_selenium_repository_name")
driver.implicitly_wait(5)
time.sleep(2)

create_repo=driver.find_element(By.XPATH,"/html/body/div[5]/main/div/form/div[5]/button")
driver.implicitly_wait(1)
create_repo.click()
time.sleep(2)


clipboard_button=driver.find_element(By.XPATH,"/html/body/div[5]/div/main/turbo-frame/div/div/git-clone-help/div[2]/div[2]/div/div/clipboard-copy")
clipboard_button.click()
value=(pyperclip.paste())
print(type(value))
print(value[22:92])
print(os.popen(f"cd.. && git clone {value[22:92]}").read())
source_path="C:/Users/jtannoury/Desktop/selenium-repository"
dst_path="C:/Users/jtannoury/Desktop/new_selenium_repository_name"
for file in os.listdir(source_path):
    if ".git" not in file and ".idea" not in file:
        shutil.copy(source_path+"/"+file,dst_path)
print(os.popen(f"cd.. && cd new_selenium_repository_name && git add .").read())
print(os.popen(f'cd.. && cd new_selenium_repository_name && git commit -m "initial commit" ').read())
print(os.popen(f"cd.. && cd new_selenium_repository_name && git push").read())

driver.get("https://github.com/")
driver.implicitly_wait(1)
try:
    new_repo=driver.find_element(By.LINK_TEXT,"jatannoury-Tradias/new_selenium_repository_name")
except:
    new_repo=driver.find_element(By.XPATH,"/html/body/div[5]/div/aside/div/loading-context/div/div[1]/div/ul/li[3]/div/div/a")
new_repo.click()
driver.implicitly_wait(1)
otc=driver.find_element(By.XPATH,"/html/body/div[5]/div/main/turbo-frame/div/div/div/div[3]/div[1]/div[3]/div[3]/div[1]/div[2]/div[2]/span/a")
otc.click()
time.sleep(2)
driver.back()

github=driver.find_element(By.XPATH,"/html/body/div[5]/div/main/turbo-frame/div/div/div/div[3]/div[1]/div[3]/div[3]/div[1]/div[3]/div[2]/span/a")
github.click()
time.sleep(5)
driver.back()

# driver.get("/html/body/div[5]/div/aside/div/loading-context/div/div[1]/div/ul[1]/li[3]/div/div/a")
time.sleep(10)