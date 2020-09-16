import sys
import io
from selenium import webdriver

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

driver = webdriver.PhantomJS(executable_path="c:/section3/webdriver/phantomjs/phantomjs")

driver.implicitly_wait(5)

driver.get('https://google.com')
driver.save_screenshot('c:/section3/img/website1.png')
driver.get('https://www.daum.net')
driver.save_screenshot('c:/section3/img/website2.png')
driver.quit()
print('screenshot complete')
