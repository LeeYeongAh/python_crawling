import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

class NameTest:
    total = 0

print(dir())
print("before : ", NameTest.__dict__)
NameTest.total = 1
print("after : ", NameTest.__dict__)

n1 = NameTest()
n2 = NameTest()

print(id(n1), "vs", id(n2))
print(dir())
print(n1.__dict__)
print(n2.__dict__)
n1.total = 88
print(n1.__dict__) # n1의 인스턴스 네임스페이스에 생김
print(n2.__dict__) # n2의 인스턴스 네임스페이스에 없음

print(n1.total) # n1의 인스턴스 네임스페이스 먼저 확인
print(n2.total) # n2의 인스턴스 네임스페이스 먼저 확인 후 클래스 네임스페이스 확인
