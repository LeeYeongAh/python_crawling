import sys
import io
import urllib.request as dw

# urlopen : 변수할당 -> 파싱 -> 저장


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

imgUrl = "https://search.pstatic.net/common/?src=http%3A%2F%2Fpost.phinf.naver.net%2F20161017_120%2F1476630494280zhkx5_PNG%2FI8fV1_cGRbtoMGrxvdIXeW5B5rTU.jpg&type=sc960_832"
htmlUrl = "http://google.com"

savePath1 = "c:/section2/test1.jpg"
savePath2 = "c:/section2/index.html"

f = dw.urlopen(imgUrl).read()
f2 = dw.urlopen(htmlUrl).read()

saveFile1 = open(savePath1, 'wb') # w, r, a
saveFile1.write(f)
saveFile1.close()

with open(savePath1, 'wb') as saveFile2:
    saveFile2.write(f2)

# with문 이용시 알아서 close() 해 준다. 얘가 더 권장됨



print("다운로드 완료!")
