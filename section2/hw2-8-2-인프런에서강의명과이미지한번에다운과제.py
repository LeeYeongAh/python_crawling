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

url = "https://www.inflearn.com/courses?order=famous"


res = req.urlopen(url).read()
savePath = "C:\\section2\\imagedownload\\"

try:
    if not (os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("폴더 만들기 실패")
        raise

soup = BeautifulSoup(res, "html.parser")
img_list = soup.select("div.card.course.course_card_item")


for i, e in enumerate(img_list, 1):
    with open(savePath+"text_"+str(i)+"student.txt", "wt") as f:
        f.write(e.select_one("div.course_title").string)
    fullFileName = os.path.join(savePath, savePath+"img_student_"+str(i)+".png")
    req.urlretrieve(e.select_one("div.card-image > figure.image > img")['src'], fullFileName)



url = "https://www.inflearn.com/courses?order=rating"


res = req.urlopen(url).read()
savePath = "C:\\section2\\imagedownload\\"

try:
    if not (os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("폴더 만들기 실패")
        raise

soup = BeautifulSoup(res, "html.parser")
img_list = soup.select("div.card.course.course_card_item")


for i, e in enumerate(img_list, 1):
    with open(savePath+"text_"+str(i)+"score.txt", "wt") as f:
        f.write(e.select_one("div.course_title").string)
    fullFileName = os.path.join(savePath, savePath+"img_score_"+str(i)+".png")
    req.urlretrieve(e.select_one("div.card-image > figure.image > img")['src'], fullFileName)



print("다운로드 완료")
