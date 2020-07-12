# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 07:24:12 2020

@author: USER
"""
#import time
#from bs4 import BeautifulSoup
#import requests
#r = requests.get("https://www.ig.com/en/forex/markets-forex")
#soup = BeautifulSoup(r.content, "html.parser")
#results = soup.findAll("span",attrs={"data-field": "CPT"})
#data=[]
#for spatn in results:
#    if spatn.text and spatn.text != '-':
#        data.append(spatn.text)
#    time.sleep(1)
#print(data)
#from selenium import webdriver
#from selenium.webdriver.common.by import By
#
#driver = webdriver.Chrome('C:\\Users\\USER\\Downloads\\chromed\\chromedriver')
#driver.get('https://www.ig.com/en/forex/markets-forex')
#
#for elm in driver.find_elements(By.CSS_SELECTOR, "span[data-field=CPT]"):
#    print(elm, elm.text)
#    
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('C:\\Users\\USER\\Downloads\\chromed\\chromedriver')
driver.get('https://www.ig.com/en/cryptocurrency-trading')


timeout = 10

try:
    WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(
            (By.XPATH,
             "//div[@class='dynamic-table__cell']")
        )
    )
except TimeoutException:
    print("Struggling to get the page....Have faith in this buggy script!")
    
data = []

while not data:
    for elm in driver.find_elements(By.CSS_SELECTOR, "span[data-field=V2-F-BID]"):
        if elm.text and elm.text != '-': # Maybe check on contains digit
            data.append(elm.text)
    time.sleep(7)

    
tet =[]
while not tet:
    for em in driver.find_elements(By.CSS_SELECTOR, "span[data-field=OFR]"):
        if em.text and em.text != '-': # Maybe check on contains digit
            tet.append(em.text)
    time.sleep(7)
print(data)
print(tet)
