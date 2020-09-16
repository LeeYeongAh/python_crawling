import sys
import io
import urllib.request as dw

# 저장 -> open('r') -> 변수 할당 -> 파싱 -> 저장
# 파싱 필요 없을 때

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

imgUrl = "https://search.pstatic.net/common/?src=http%3A%2F%2Fpost.phinf.naver.net%2F20161017_120%2F1476630494280zhkx5_PNG%2FI8fV1_cGRbtoMGrxvdIXeW5B5rTU.jpg&type=sc960_832"
htmlUrl = "http://google.com"

savePath1 = "c:/section2/test1.jpg"
savePath2 = "c:/section2/index.html"
#urllib.request.urlretrieve(imgUrl, savePath)
dw.urlretrieve(imgUrl, savePath1)
dw.urlretrieve(htmlUrl, savePath2)
print("다운로드 완료!")
