from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from config import *


def send_tg_message(token, chat_id, text):
    url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
    response = requests.get(url)
    return response


def monitoring_google_maps(driver, urls):
    for url in urls:
        driver.get(url)
        try:
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/span[1]/span/span/span[2]/span[1]/button')))
            views_text = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/span[1]/span/span/span[2]/span[1]/button').text
        except:
            print(url + ' Not Found')

        temp = filter(str.isdigit, views_text) # Получили filter object
        views_count = int("".join(temp))
        print(views_count)
        if views_count > old_views_count[url] and old_views_count[url] != -1:
            send_tg_message(TOKEN, chat_id, 'Новый отзыв на '+url)
        old_views_count[url] = views_count
        print(old_views_count[url])


chrome_options = Options()
#chrome_options.add_argument('--headless')
#chrome_options.add_argument('--disable-gpu')
#chrome_options.add_experimental_option("prefs", {'profile.managed_default_content_settings.javascript': 2})
driver = webdriver.Chrome('chromedriver', chrome_options=chrome_options)

urls = []
with open('urls/google.txt') as f:
    for l in f:
        urls.append(l)

old_views_count = {}
for url in urls:
    old_views_count[url] = -1

monitoring_google_maps(driver, urls)