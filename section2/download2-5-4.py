from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

html = """
<html><body>
<div id="main">
  <h1>강의목록</h1>
  <ul class="lecs yoho">
    <li>Java 초고수 되기</li>
    <li>파이썬 기초 프로그래밍</li>
    <li>파이썬 머신러닝 프로그래밍</li>
    <li>안드로이드 블루투스 프로그래밍</li>
  </ul>
</div>
</body></html>
"""
soup = BeautifulSoup(html, 'html.parser')
h1 = soup.select("div#main > h1") # list로 반환함
print('h1', h1)

for h in h1: # 하나일지라도 list로 반환되어서 저렇게 해야해
    print(h.string)


h1_ = soup.select_one("div#main > h1")
print('h1_',h1_.string)

list_li = soup.select("div#main > ul.lecs.yoho > li")
for li in list_li:
    print("li >>",li.string)
