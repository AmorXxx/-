from selenium import webdriver
import sys
a = eval(sys.argv[1])
browser = webdriver.Chrome()
browser.get('http://60.219.165.24')
username = browser.find_element_by_name('zjh')
username.send_keys(a)
username = browser.find_element_by_name('mm')
username.send_keys('1')
btn = browser.find_element_by_id('btnSure')
btn.click()
browser.switch_to.frame(browser.find_element_by_xpath(
    "//frame[@src='/menu/s_top.jsp']"))
name = browser.find_element_by_xpath("/html/body/table[1]/tbody/tr/td[2]/table/tbody"
                                     "/tr[1]/td/table/tbody/tr/td")
print(name.text[6:-6])
