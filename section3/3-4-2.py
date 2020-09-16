import sys
import io
import requests
from bs4 import BeautifulSoup
import urllib.parse as rep
import urllib.request as req
import os
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 로그인 유저정보
LOGIN_INFO = {'email': "id", 'password': "pw"}

# Session 생성, with 구문 안에서 유지
with requests.Session() as s:
    login_req = s.post('https://www.inflearn.com/api/signin', data=LOGIN_INFO)
    #HTML 소스 확인
    #print("login_req", login_req.text)
    # Header 확인
    #print('headers', login_req.headers)
    if login_req.status_code == 200 and login_req.ok:
        post_one = s.get('https://www.inflearn.com/my-courses')
        post_one.raise_for_status()
        soup = BeautifulSoup(post_one.text, "html.parser")
        #print(soup.prettify())
        #print(article)
        courses_img = soup.select("div.columns.is-mobile.courses_card_list_body.is-multiline img")
        for i, ci in enumerate(courses_img,1):
            #print(ci)
            fullFileName = os.path.join("C:\\section3\\", str(i)+'.jpg')
            req.urlretrieve(ci['src'], fullFileName)
