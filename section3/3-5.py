import sys
import io
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import re
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
#요청 url
url = 'https://www.wishket.com/accounts/login/'

# fake user-agent 생성
ua = UserAgent()


with requests.Session() as s:
    #url 연결
    s.get(url)
    #login 정보 payload
    LOGIN_INFO = {
        'identification': 'id',
        'password': 'pw',
        'csrfmiddlewaretoken': s.cookies['csrftoken']
    }

    #요청
    response = s.post(url, data=LOGIN_INFO, headers={'User-Agent': str(ua.chrome), 'referer': 'https://www.wishket.com/accounts/login/'})
    #HTML 결과 확인
    #print('response', response.text)
    if response.status_code == 200 and response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
        projectList = soup.select('div.user-project > div')

        for i, e in enumerate(projectList,1):
            front = str(e)
            front = re.sub('<.+?>', ' ', front, 0).strip().split()
            temp = front.copy()
            front = (' '.join(temp[:-1]))
            tail = temp[-1]
            print(i, front, tail)
