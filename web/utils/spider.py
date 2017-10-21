from bs4 import BeautifulSoup as bs
from login import login
import requests

"""
"18317857703", "dorahack123"
"""

def spider(uid, pwd):
    login_cookies = login(uid, pwd)
    s = requests.Session()

    for cookie in login_cookies:
        c = requests.cookies.RequestsCookieJar()
        c.set(cookie['name'], cookie['value'], path=cookie['path'], domain=cookie['domain'])

        s.cookies.update(c)
    print(s.cookies)
    r = requests.get("https://i.youku.com/", cookies = s.cookies)

    print(r.text)
