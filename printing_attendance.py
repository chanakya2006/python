from selenium import webdriver 
from time import *
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.select import Select
from bs4 import BeautifulSoup
from os import *


def append_marks(driver,value):
    dropdown.select_by_value(value)
    page = driver.page_source
    soup = BeautifulSoup(page,"lxml")
    percentage = soup.find_all("td")[-1].text
    subject = (soup.find_all("h2")[1].text)[23:]
    return [subject,percentage]

driver = webdriver.Edge() 
driver.get("https://aiveda.tech/dtcdashboard/login.php") 
driver.find_element(by=By.NAME, value="username").send_keys("The username") # Change The username to your email id 
driver.find_element(by=By.NAME, value="password").send_keys("The password") # Change The password to your password
driver.find_element(by=By.ID, value="student").click()
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
driver.execute_script("loadIframe('student_dashboardtesting.php')")
driver.switch_to.frame("contentIframe")
dropdown = Select(driver.find_element(by=By.ID,value="subject"))
l = []
for i in dropdown.options:
    l.append(i.get_attribute("value"))
l.pop(0)

attendance = {}
system("cls")
for k in l:
    dropdown = Select(driver.find_element(by=By.ID,value="subject"))
    t = append_marks(driver=driver,value=k)
    attendance[t[0]] = t[1]

driver.quit()



for i in attendance:
    print(i+" : "+attendance[i])


"""
For the program to run on your device you need run the following commands first on your command prompt (I am assuming you have python set up already):
pip install selenium
pip install beautifulsoup4
"""