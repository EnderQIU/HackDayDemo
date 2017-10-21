from bs4 import BeautifulSoup as bs
import requests

s = requests.Session()

s.cookies = []

s.get("https://i.youku.com/i/UNTM3NzUwNTMy")

res = s.request('GET', "https://i.youku.com/i/UNTM3NzUwNTMy")

parsed = bs(res.text)



