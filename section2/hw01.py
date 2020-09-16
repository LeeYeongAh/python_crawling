import sys
import io
import urllib.request as req
from urllib.parse import urlencode

# urlopen : 변수할당 -> 파싱 -> 저장


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')



API = "https://siape.veta.naver.com/fxclick"
values ={
    "eu":"EU10041892",
    "calp" : "-",
    "oj":"ZagUyei1lSgOWdeqzmpSTXGPnKkh%2FoRNBazN69ObGo1Se5T8tLrden3MvdjVKAV1ht2So1LWEJfYQAea7u4%2BIFMhppu31PHobMhMtQmbJCE",
    "ac":"8135768",
    "src":"4529484",
    "br":"3225204",
    "evtcd":"P901",
    "x_ti":"1316",
    "tb":"",
    "oid":"",
    "sid1":"",
    "sid2":"",
    "rk":"b5b4ba8fc5a1acc03764536d8899f7ba",
    "eltts":"bYJLFAD3M8%2FI86eghpCnEg%3D%3D",
    "lu":"",
    "brs":"Y"
}

params = urlencode(values)


imgUrl = "https://ssl.pstatic.net/tveta/libs/1295/1295424/5d90a8c1cf43a3b9bf41_20200904151804396.jpg"
url = API+"?"+params+"&"


savePath1 = "c:/section2/hw01.jpg"
savePath2 = "c:/section2/hw01.mp4"

f = req.urlopen(imgUrl).read()
f2 = req.urlopen(url).read()


with open(savePath1, 'wb') as saveFile1:
    saveFile1.write(f)

with open(savePath2, 'wb') as saveFile2:
    saveFile2.write(f2)
print("다운로드 완료!")
