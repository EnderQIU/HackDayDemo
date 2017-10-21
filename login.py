#/usr/bin/python
# -*- coding: utf-8 -*-

USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/61.0.3163.100 Chrome/61.0.3163.100 Safari/537.36"
HEADERS = {"User-Agent": USER_AGENT}

from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.PhantomJS()
try:
    driver.get('http://www.youku.com/')
    login = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'avatar')))
    login.click()
    try:
        login_frame = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'YT-loginFramePop')))
        username = WebDriverWait(login_frame, 20).until(EC.presence_of_element_located((By.ID, 'YT-ytaccount')))
        username.send_keys('825942030@qq.com')
        password = WebDriverWait(login_frame, 20).until(EC.presence_of_element_located((By.ID, 'YT-ytpassword')))
        password.send_keys('zhou88270273')
        login_buttom = WebDriverWait(login_frame, 20).until(EC.presence_of_element_located((By.ID, 'YT-nloginSubmit')))
        login_buttom.click()
        try:
            cookies = driver.get_cookies()
            print(cookies)
        except Exception as e:
            print(e)
    except Exception as e:
        print(e)
except Exception as e:
    print(e)
