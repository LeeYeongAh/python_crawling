import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.keys import Keys
import pyperclip
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class NcafeMemberExt:
    #초기화실행(webdriver)
    def __init__(self):
        #chrome_options = Options()
        #chrome_options.add_argument("--headless") #CLI
        #self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="C:/section3/webdriver/chrome/chromedriver")
        self.driver = webdriver.Chrome(executable_path="c:/section3/webdriver/chrome/chromedriver")

        self.driver.implicitly_wait(5)

    #네이버 카페 회원 정보 추출
    def getMemberList(self):
        self.driver.get('https://www.naver.com')
        login_btn = self.driver.find_element_by_class_name('link_login')
        login_btn.click()
        time.sleep(1)
        tag_id = self.driver.find_element_by_name('id')
        tag_pw = self.driver.find_element_by_name('pw')
        tag_id.clear()
        time.sleep(1)
        tag_id.click()
        pyperclip.copy('id')
        tag_id.send_keys(Keys.CONTROL, 'v')
        time.sleep(1)
        tag_pw.click()
        pyperclip.copy('pw')
        tag_pw.send_keys(Keys.CONTROL, 'v')
        time.sleep(1)
        login_btn = self.driver.find_element_by_id('log.login')
        login_btn.click()
        time.sleep(1)
        #self.driver.implicitly_wait(1)
        self.driver.get('https://cafe.naver.com/CafeMemberViewTab.nhn?defaultSearch.clubid=30227214')
        self.driver.implicitly_wait(30)
        self.driver.switch_to_frame('cafe_main')
        print('test', self.driver.page_source)
        time.sleep(3)
        soup = BeautifulSoup(self.driver.page_source,'html.parser')
        #print(soup.prettify())
        return soup.select('div.mem_list_wrap > ul div.ellipsis.m-tcol-c')

    def printMemberList(self, list):
        f = open("c:/section3/memberList.txt", 'wt')
        for i in list:
            f.write(i.string.strip()+'\n')
            print(i.string.strip())
        f.close()

    def __del__(self):
        self.driver.quit()
        #self.driver.close()
        print("removed driver object")

if __name__=='__main__':
    a = NcafeMemberExt()
    start_time = time.time()
    a.printMemberList(a.getMemberList())
    print("--total %s seconds--" %(time.time()- start_time))
    del a
