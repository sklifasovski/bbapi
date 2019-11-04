from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import re
chromedriver = 'e:/chromedriver.exe'
e = DesiredCapabilities.CHROME
e['goog:loggingPrefs'] = { 'driver':'DEBUG'}
options = webdriver.ChromeOptions()
browser = webdriver.Chrome(executable_path=chromedriver, chrome_options=options, desired_capabilities=e)
browser.get('https://alpari.com/ru/login/')
email = browser.find_element_by_id('authorization_login')
password = browser.find_element_by_id('authorization_password')
button = browser.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div[3]/div[1]/div[3]/button')
email.send_keys('sklifasovski@live.ru')
password.send_keys('PkjqLbvf123')
button.click()
time.sleep(30)
browser.get('https://my.alpari.com/ru/platforms/fix-contractstrader/')
requiredHtml = browser.page_source
import json
from pprint import pprint
i = 0
tic=[]
ii = input('Стартуем? Y/N')
while i<10 and ii=='Y':
    for entry in browser.get_log('driver'):
        if '"value": "Creating imaginary bar:' in entry['message']:
            a = re.findall('(\d+)', entry['message'][460:475])
            b=float(a[0] + '.' + a[1])
            print('%.5f' % b)
            tic.append('%.5f' % b)
            print(tic)
            if len(tic)>=3:
                second1 = tic[-2]
                second2 = tic[-1]
                if second1<second2:
                    print('Последняя ниже')

                if second1 > second2:
                    print('Последняя выше')

                if second1 == second2:
                    print('Последняя равна')

            if len(tic)>=3:
                second1 = tic[-2]
                second2 = tic[-3]
                if second1<second2:
                    print('Предпоследняя ниже')
                if second1 > second2:
                    print('Предпоследняя выше')
                if second1 == second2:
                    print('Предпоследняя равна')
            if len(tic)>=4:
                second1 = tic[-3]
                second2 = tic[-4]
                if second1<second2:
                    print('Третья ниже')

                if second1 > second2:
                    print('Третья выше')

                if second1 == second2:
                    print('Третья равна')





