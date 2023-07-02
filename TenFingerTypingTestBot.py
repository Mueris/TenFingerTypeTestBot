# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 13:03:38 2023

@author: musta
"""
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time


Path ="C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(Path)
url="https://www.m5bilisim.com/tr/on-parmak/hiz-testi/"
def startWriting():
    
    dataField=driver.find_element(By.ID, 'yaziyaz')
    dataToEnter=driver.find_element(By.XPATH,'//div[@id="satir"]')
    timeField=driver.find_element(By.XPATH, '//span[@id="zaman"]')
    innerhtml=dataToEnter.get_attribute('innerHTML')
    dataSoup=BeautifulSoup(innerhtml,'html.parser')
    all_tags = [tag for tag in dataSoup.find_all()]
    total_time=60
    for tag in all_tags:
        total_time=timeField.text
        timeR=(int(total_time.split(':')[0])*60)+int(total_time.split(':')[1])
        if(tag.name=='span'and timeR>=1):
            data=tag.text
            print(data)
            dataField.send_keys(data+" ")
          
    timeR=(int(total_time.split(':')[0])*60)+int(total_time.split(':')[1])   
    if (timeR!=0):
        time.sleep(timeR)
        print("Completed")
def wordSize(size):
    driver.get(url)
    time.sleep(1)
    changeButton=driver.find_element(By.XPATH,'//span[@id="mcab"]')
    changeButton.click()
    time.sleep(0.5)
    if(size>=200):#if user wants more then 200 words then selects 1000 words on web site
        thousand=driver.find_element(By.XPATH, '//a[@href="javascript:dolapDegistir(2)"]')
        thousand.click()
        
    else:#if user wants less then 200 words then selects 200 words on web site
        houndred=driver.find_element(By.XPATH,'//a[@href="javascript:dolapDegistir(1)"]')
        houndred.click()
    time.sleep(0.5)
    startWriting()
#size = int(input('Please Enter the word size you want (200 or 1000)'))    
wordSize(1000)



    