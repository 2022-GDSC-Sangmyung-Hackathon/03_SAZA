from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait

# --크롬창을 숨기고 실행-- driver에 options를 추가해주면된다
# options = webdriver.ChromeOptions()
# options.add_argument('headless')

def get_reviews(dong, name): 
    url = 'https://map.naver.com/v5/search'
    driver = webdriver.Chrome('restaurant/register_functions/chromedriver')
    query = dong + " " + name
    driver.get(f"https://map.naver.com/v5/search/{query}?c=14203933.7141038,4562681.4505997,10,0,0,0,dh")

    sleep(3)

    driver.switch_to.frame("entryIframe")

    visitor_reviews = driver.find_element(By.CSS_SELECTOR, "#app-root > div > div > div > div.place_section.GCwOh > div._3uUKd._2z4r0 > div._20Ivz > span:nth-child(2) > a > em").text
    blog_reviews = driver.find_element(By.CSS_SELECTOR, "#app-root > div > div > div > div.place_section.GCwOh > div._3uUKd._2z4r0 > div._20Ivz > span:nth-child(3) > a > em").text
    
    return visitor_reviews, blog_reviews

