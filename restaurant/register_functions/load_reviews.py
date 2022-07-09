from restaurant.models import Restaurant

from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
import json
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException

driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(3)

naver_url = "https://map.naver.com/"
driver.get(naver_url)

rs = Restaurant.objects.all()

for r in rs:

    query = r.dong + r.name

    driver.find_element_by_xpath('//*[@id="search-input"]').clear()
    driver.find_element_by_xpath('//*[@id="search-input"]').send_keys(query)
    driver.find_element_by_xpath('//*[@id="header"]/div[1]/fieldset/button').click()

    try:
    click = driver.find_element_by_xpath("//*[@id='panel']/div[2]/div[1]/div[2]/div[2]/ul/li[1]/div[1]/dl")
    if store_name in click.text:
        click.click()
    else:
        print("--해당음식점이 없습니다")
        continue
            
    try:
        driver.find_element_by_xpath("//*[@id='panel']/div[2]/div[1]/div[2]/div[2]/ul/li[1]/div[2]/ul/li[4]/a").click()
    except ElementNotVisibleException:
        driver.find_element_by_xpath("//*[@id='panel']/div[2]/div[1]/div[2]/div[2]/ul/li[1]/div[1]/dl").click()
        driver.find_element_by_xpath("//*[@id='panel']/div[2]/div[1]/div[2]/div[2]/ul/li[1]/div[2]/ul/li[4]/a").click()
        
    
except NoSuchElementException:
    print('--검색결과가 없습니다')
        
    query2 = data2['hits'][i]['_source']['상호명']+" " + data2['hits'][i]['_source']['도로명주소'].split(' ')[1]

    driver.find_element_by_xpath('//*[@id="search-input"]').clear()
    driver.find_element_by_xpath('//*[@id="search-input"]').send_keys(query2)
    driver.find_element_by_xpath('//*[@id="header"]/div[1]/fieldset/button').click()

    try:
        click = driver.find_element_by_xpath("//*[@id='panel']/div[2]/div[1]/div[2]/div[2]/ul/li[1]/div[1]/dl")
        if store_name in click.text:
            click.click()
        else:
            print("--해당음식점이 없습니다")
            continue
        
        try:
            driver.find_element_by_xpath("//*[@id='panel']/div[2]/div[1]/div[2]/div[2]/ul/li[1]/div[2]/ul/li[4]/a").click()
        except ElementNotVisibleException:
            driver.find_element_by_xpath("//*[@id='panel']/div[2]/div[1]/div[2]/div[2]/ul/li[1]/div[1]/dl").click()
            driver.find_element_by_xpath("//*[@id='panel']/div[2]/div[1]/div[2]/div[2]/ul/li[1]/div[2]/ul/li[4]/a").click()

    except NoSuchElementException:
        print('--검색결과가 없습니다')
        continue