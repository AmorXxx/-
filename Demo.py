# -*- coding: utf-8 -*
"""
author: Amor

finished: 2019-5-30

"""
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from MySQLComm import MySQLCommand
"""成绩查询"""


def grade(zhanghao, mima):
    """该列表用于储存每科详细信息的字典"""
    grade_list = []
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    # 上面三行代码就是为了将Chrome不弹出界面，实现无界面爬取
    chrome_options.add_argument('--disable-gpu')
    browser = webdriver.Chrome(chrome_options=chrome_options)
    # noinspection PyBroadException
    try:

        browser.get('http://60.219.165.24')
        username = browser.find_element_by_name('zjh')
        username.send_keys(zhanghao)
        username = browser.find_element_by_name('mm')
        username.send_keys(mima)
        browser.find_element_by_id('btnSure').click()
        browser.switch_to.frame(browser.find_element_by_name('bottomFrame'))
        browser.switch_to.frame(browser.find_element_by_name('mainFrame'))
        browser.find_element_by_link_text('方案成绩').click()
        time.sleep(1)
        browser.switch_to.default_content()
        browser.switch_to.frame(browser.find_element_by_name('bottomFrame'))
        browser.switch_to.frame(browser.find_element_by_name('menuFrame'))
        browser.find_element_by_link_text('本学期成绩查询').click()
        browser.switch_to.default_content()
        browser.switch_to.frame(browser.find_element_by_name('bottomFrame'))
        browser.switch_to.frame(browser.find_element_by_name('mainFrame'))
        table = browser.find_element_by_class_name('displayTag')
        rows = table.find_elements_by_tag_name('tr')
        for row in rows[1:]:
            cols = row.find_elements_by_tag_name('td')
            """该字典用于储存每科的详细信息"""
            my_list = {
                'id': 0,
                'stu_no': zhanghao,
                'course_no': cols[0].text,
                'score': cols[6].text,
                'course_type': cols[5].text,
                'course_name': cols[2].text,
                'count': cols[4].text,
                'send': 0
            }
            grade_list.append(my_list)
    except Exception:
        print('Password is INCORRECT! The stu_no is ' + zhanghao)
    finally:
        browser.close()
        return grade_list


def main():
    print('Spider Launching!!!!')
    mysqlCommand = MySQLCommand()
    mysqlCommand.connectMysql()
    res = mysqlCommand.getStuNo()
    for row in range(0, 600):
        zhanghao = res[row][0]
        mysqlCommand.insertData(grade(zhanghao, 1))
    mysqlCommand.closeMysql()


if __name__ == '__main__':
    main()

