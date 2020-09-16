import sys
import io
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

firefox_options = Options()
firefox_options.add_argument('--headless') #cli

driver = webdriver.Firefox(firefox_options=firefox_options,executable_path="c:/section3/webdriver/firefox/geckodriver")
#driver.set_window_size(1920,1280)
#driver.implicitly_wait(5)

driver.get('https://google.com')
#time.sleep(5)
driver.save_screenshot('c:/section3/img/website1_cli3.png')

driver.get('https://www.daum.net')
#time.sleep(5)
driver.save_screenshot('c:/section3/img/website2_cli2.png')
driver.quit()
print('screenshot complete')
