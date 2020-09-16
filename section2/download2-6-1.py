from bs4 import BeautifulSoup
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

html = """
<html><body>
  <ul>
    <li id="naver"><a href="http://www.naver.com">naver</a></li>
    <li><a href="http://www.daum.net">daum</a></li>
    <li><a href="http://www.daum.com">daum</a></li>
    <li><a href="https://www.google.com">google</a></li>
    <li><a href="https://www.tistory.com">tistory</a></li>
  </ul>
</body></html>
"""

soup = BeautifulSoup(html,'html.parser')
"""
test = soup.find('a',string='naver')
print(test.string)
"""

print(soup.find(id='naver').string)
li = soup.findAll(href=re.compile(r"^https://"))
li2 = soup.findAll(href=re.compile("da"))
print('li >>', li)

for e in li2:
    print(e.attrs['href'])
