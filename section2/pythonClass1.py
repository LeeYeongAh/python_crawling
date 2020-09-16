import io
import sys



sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

class UserInfo:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def print_info(self):
        print("------------")
        print("Name: " + self.name)
        print("Phone: " + self.phone)
        print("------------")

    def __del__(self):
        print("del 발생")

user1 = UserInfo("kim","0-1-0")
user2 = UserInfo("lee","0-1341-0")

#print(id(user1))
#print(id(user2))

"""user1.set_info("kim","-1-")
user2.set_info("lee","-1341-")"""

user1.print_info()
user2.print_info()

print(user1.__dict__)
print(user2.__dict__)
"""
{'phone': '-1-', 'name': 'kim'}
{'phone': '-1341-', 'name': 'lee'}
"""

print(user1.phone)
"""-1-"""


class SelfTest:
    def func1():
        print("1 called")
    def func2(self):
        #print(id(self))
        print("2 called")

f = SelfTest()
#print(dir(f))
print(id(f))

f.func2()
SelfTest.func1()
