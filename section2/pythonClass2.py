import io
import sys



sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

class UserInfo:
    def set_info(self, name, phone):
        self.name = name
        self.phone = phone

    def print_info(self):
        print("------------")
        print("Name: " + self.name)
        print("Phone: " + self.phone)
        print("------------")

user1 = UserInfo()
user2 = UserInfo()

#print(id(user1))
#print(id(user2))

user1.set_info("kim","-1-")
user2.set_info("lee","-1341-")

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
