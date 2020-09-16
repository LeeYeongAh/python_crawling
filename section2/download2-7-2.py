import io
import json
import sys
import urllib.request as req
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

url = "https://finance.naver.com/sise/"
res = req.urlopen(url).read().decode('euc-kr')
soup = BeautifulSoup(res, "html.parser")

top10 = soup.select("table#siselist_tab_0 > tr")
i=1
for e in top10:
    if e.find("a") is not None:
        print(i,e.select_one(".tltle").string)
        i+=1
