from selenium import webdriver
import time
import json
"""成绩查询"""


def grade(zhanghao, mima):
    """该列表用于储存每科详细信息的字典"""
    grade_list = []
    # noinspection PyBroadException
    try:
        browser = webdriver.Chrome()
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
        for row in rows[1:-1]:
            cols = row.find_elements_by_tag_name('td')
            """该字典用于储存每科的详细信息"""
            new_dict = {
                'xh': zhanghao,
                'kcdm': cols[0].text,
                'cj': cols[6].text,
                'kcxz': cols[5].text,
                'kcmc': cols[2].text,
                'xf': cols[4].text
            }
            grade_list.append(new_dict)
    except Exception:
        grade_list.append("用户名或密码错误，请重新输入！")
    finally:
        final_dict = {
            "data": grade_list,
            "context": "grade"
        }
        browser.close()
        return json.dumps(final_dict, ensure_ascii=False)


# test

