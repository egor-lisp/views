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


def monotoring_yandex_maps(driver, urls):
    for url in urls:
        driver.get(url)
        try:
            views_text = driver.find_element_by_class_name('business-header-rating-view__text').text
        except:
            print(url + ' Not Found')
        temp = filter(str.isdigit, views_text) # Получили filter object
        views_count = int("".join(temp))
        if views_count > old_views_count[url] and old_views_count[url] != -1:
            send_tg_message(TOKEN, chat_id, 'Новый отзыв на '+url)
        old_views_count[url] = views_count
        print(old_views_count[url])


chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_experimental_option("prefs", {'profile.managed_default_content_settings.javascript': 2})
driver = webdriver.Chrome('/usr/local/bin/chromedriver', chrome_options=chrome_options)

urls = []
with open('urls/yandex.txt') as f:
    for l in f:
        urls.append(l)

old_views_count = {}
for url in urls:
    old_views_count[url] = -1

while True:
    monotoring_yandex_maps(driver, urls)
