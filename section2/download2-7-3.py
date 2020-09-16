import io
import json
import sys
import urllib.request as req
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import urllib.parse as rep

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

url = "https://www.inflearn.com/"
res = req.urlopen(url).read()
soup = BeautifulSoup(res, "html.parser")


recommend = soup.select("div.course_title")

for i, e in enumerate(recommend,1):
    print(i, e.string)
