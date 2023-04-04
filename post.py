from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time

url = "https://www.instagram.com/login/"

browser = webdriver.Edge()
browser.get(url)

time.sleep(1)


#/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button
browser.find_element(By.NAME, 'username').send_keys('artistic_space8')
#browser.find_element(By.NAME, 'password').send_keys('password')
#WebDriverWait(browser,6).until(EC.element_to_be_clickable((By.XPATH,\
 #   '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button'))).click()


time.sleep(1)
browser.find_element(By.NAME, 'password').send_keys('tinaa@19', Keys.ENTER)

WebDriverWait(browser,3).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div'))).click()

WebDriverWait(browser,3).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/span/a'))).click()
#/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]
WebDriverWait(browser,3).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]'))).click()
#/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[7]/div/div/a/div
WebDriverWait(browser,3).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[7]/div/div/a/div'))).click()

WebDriverWait(browser,3).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]/div/button'))).click()
time.sleep(1000)

#/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]/div/button