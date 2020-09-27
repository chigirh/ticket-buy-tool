# 時刻関連
import schedule
import time

import datetime
import schedule
from datetime import timedelta
import time

# selenium
from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

import requests
from bs4 import BeautifulSoup
import math

import json
import os

import traceback


options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--lang=ja')
options.add_argument('--blink-settings=imagesEnabled=false')

#設定ファイル

json_file= open('conf.json', 'r')
conf_data = json.load(json_file)

login_url = conf_data['login_url']
page_url = conf_data['buy_url']

email = conf_data['mail']
password = conf_data['password']

start_time = conf_data['launched_time']

ticket_type_idxd = int(conf_data['ticket_type'])
ticket_num = conf_data['ticket_num']

cvs_type = conf_data['cvs_type']

#driver = webdriver.Chrome(chrome_options=options)
driver = webdriver.Chrome()
driver.implicitly_wait(2)


# 標準時刻とPC内のズレの補正
start1 = datetime.datetime.strptime(start_time, '%H:%M:%S').time()
start2 = datetime.datetime.combine(datetime.date.today(), start1) - datetime.timedelta(minutes=1)
login_time = start2.strftime("%H:%M:%S")


r = requests.get('https://ntp-a1.nict.go.jp/cgi-bin/jst')
soup = BeautifulSoup(r.text,'lxml')

t1 = soup.find("body").string
t2 = t1.rstrip('\n')
t3 = time.time()
t4 = float(t2)-t3

if t4 >= 0:
    t5 = 0
    t6 = math.ceil(t4)
    t7 = t4 - t6

else:
    t5 = -t4
    t6 = 0
    t7 = 0

start5 = datetime.datetime.combine(datetime.date.today(), start1) + datetime.timedelta(seconds = t6)
buy_time = start5.strftime("%H:%M:%S")

print('ログイン時刻' + login_time)
print('購入開始時刻' + buy_time)

# ログイン処理
def login_job():
    
    cur_time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")

    print('ログイン実行('+ cur_time +')')

    driver.get(login_url)
    driver.find_element_by_id("email").send_keys(email)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_name("action").send_keys(Keys.ENTER)

    cur_time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")

    print('ログイン完了('+ cur_time +')')


# 購入処理
def buy_job():

    print('ticket_type_idxd : '+str(ticket_type_idxd))
    print('ticket_num : '+ticket_num)

    cur_time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    print('購入開始('+ cur_time +')')

    buy_main()
    
    cur_time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    print('購入完了('+ cur_time +')')

    driver.quit()

def buy_main():
    try:
        driver.get(page_url)

        num_element = driver.find_elements_by_xpath("//select[contains(@id, 'ticket')]")[ticket_type_idxd]
        num_select_element = Select(num_element)
        num_select_element.select_by_value(ticket_num)


        wait = WebDriverWait(driver, 2)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="submit"]/p[3]/button')))
        element.click()

        driver.find_element_by_id("other_payment_method_select_img").click()
        
        cvs_element = driver.find_element_by_xpath('//*[@id="cvs_select"]')
        cvs_select_element = Select(cvs_element)
        cvs_select_element.select_by_value(cvs_type)

        wait = WebDriverWait(driver, 2)
        buy_element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="submit-btn"]/button/span')))
        buy_element.click()

        #driver.find_element_by_xpath('//*[@id="submit-btn"]/button/span').click()
    except Exception as e:
        print("例外args:", e.args)
        print('再試行')
        buy_main()

    
schedule.every().day.at(login_time).do(login_job)  
schedule.every().day.at(buy_time).do(buy_job)
cnt = 0
print('待機中')
while True:
    if(20 < cnt):
        print('待機中')
        cnt = 0
    else:
        cnt +=1

    schedule.run_pending()
    time.sleep(0.1)