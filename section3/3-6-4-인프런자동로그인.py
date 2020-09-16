import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.keys import Keys

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#chrome_options = Options()
#chrome_options.add_argument('--headless') #cli

#driver = webdriver.Chrome(chrome_options=chrome_options,executable_path="c:/section3/webdriver/chrome/chromedriver")
driver = webdriver.Chrome(executable_path="c:/section3/webdriver/chrome/chromedriver")


driver.get('https://www.inflearn.com/')

driver.implicitly_wait(3)

element = driver.find_element_by_xpath('//*[@id="header"]/nav/div[1]/div/div[3]/a[1]')
driver.execute_script("arguments[0].click()",element)
driver.find_element_by_class_name('input.email').send_keys('id')
driver.implicitly_wait(1)
driver.find_element_by_class_name('input.pwd').send_keys('pw')
driver.implicitly_wait(1)
driver.find_element_by_xpath('/html/body/div[1]/div[4]/section/form/button').click()

print('screenshot complete')
