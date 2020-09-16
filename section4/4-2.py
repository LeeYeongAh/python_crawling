import sys
import io
import urllib.request as req
from bs4 import BeautifulSoup
import os.path

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

#다운로드 url
url = "https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
savename = 'c:/section4/forecast.xml'

if not os.path.exists(savename):
    req.urlretrieve(url, savename)
    print('다운로드함')

#BeautifulSoup 파싱

xml = open(savename,'r',encoding='utf-8').read()
soup = BeautifulSoup(xml,'html.parser')
info = {}
#지역확인
for location in soup.findAll('location'):
    loc = location.find('city').string
    #print(loc)
    weather = location.findAll('tmn')
    #print(weather)
    if not (loc in info):
        info[loc] = []
    for tmn in weather:
        info[loc].append(tmn.string)
#print(info)

with open('c:/section4/forecast.txt','wt') as f:
    for loc in sorted(info.keys()):
        f.write(str(loc)+'\n')
        for n in info[loc]:
            f.write('\t'+str(n)+'\n')
