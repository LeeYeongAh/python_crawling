import io
import os
import json
import sys
import urllib.request as req
import urllib.parse as rep
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

base = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
quote = rep.quote_plus("사자") #여기에 검색어 변경하면 그때그때 다른 이미지 받을 수 
url = base + quote

res = req.urlopen(url)
savePath = "C:\\section2\\imagedownload"

try:
    if not (os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("폴더 만들기 실패")
        raise

soup = BeautifulSoup(res, "html.parser")
img_list = soup.select("div.img_area._item > a.thumb._thumb > img")

print("test", img_list)

for i, img in enumerate(img_list, 1):
    #rint(img['data-source'])
    fullFileName = os.path.join(savePath, savePath+str(i)+".jpg")
    print(fullFileName)
    req.urlretrieve(img['data-source'], fullFileName)

print("다운로드 완료")
