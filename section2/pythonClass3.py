import io
import sys



sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

#클래스 변수와 인스턴스 변수
"""
인스턴스 변수는 공유 x
클래스 변수는 공유

인스턴스에서 클래스 변수 접근 가능함
"""

class Warehouse:
    stock_num = 0
    def __init__(self, name):
        self.name = name
        Warehouse.stock_num += 1

    def __del__(self):
        Warehouse.stock_num -= 1

user1 = Warehouse('kim')
user2 = Warehouse('lee')

print(user1.name)
print(user2.name)

print(user1.__dict__) # stock_num 없다
print(user2.__dict__)
print(Warehouse.__dict__) # stock_num = 2
# 인스턴스의 네임스페이스 확인 -> 없으면 클래스 네임스페이스 확인
# 클래스 변수 (공유)
print(user1.stock_num)
print(user2.stock_num)
