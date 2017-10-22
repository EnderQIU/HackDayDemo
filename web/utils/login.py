#/usr/bin/python
# -*- coding: utf-8 -*-

USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/61.0.3163.100 Chrome/61.0.3163.100 Safari/537.36"
HEADERS = {"User-Agent": USER_AGENT}

from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def login(uid, pwd):
    driver = webdriver.Chrome()
    try:
        driver.get('http://www.youku.com/')
        login = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'avatar')))
        login.click()
        try:
            login_frame = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'YT-loginFramePop')))
            username = WebDriverWait(login_frame, 20).until(EC.presence_of_element_located((By.ID, 'YT-ytaccount')))
            username.send_keys(uid)
            password = WebDriverWait(login_frame, 20).until(EC.presence_of_element_located((By.ID, 'YT-ytpassword')))
            password.send_keys(pwd)
            login_buttom = WebDriverWait(login_frame, 20).until(
                EC.presence_of_element_located((By.ID, 'YT-nloginSubmit')))
            login_buttom.click()
            try:
                login = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'avatar')))
                login.click()
                cookies = driver.get_cookies()
                return cookies
            except Exception as e:
                print(e)
        except Exception as e:
            print(e)
    except Exception as e:
        print(e)
