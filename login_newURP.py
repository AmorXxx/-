from selenium import webdriver
import pyautogui
import time
import requests
from selenium.webdriver.common.action_chains import ActionChains
import json

def main():
    driver = webdriver.Chrome()
    driver.get("http://222.171.146.55/login")
    img = driver.find_element_by_id('captchaImg')
    time.sleep(2)
    action = ActionChains(driver).move_to_element(img)  # 移动到该元素
    action.context_click(img)  # 右键点击该元素
    action.perform()  # 执行保存
    pyautogui.typewrite(['down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter', 'enter'])
    time.sleep(1)
    pyautogui.typewrite(['enter'])
    username = driver.find_element_by_id('input_username')
    username.send_keys("2016026358")
    password = driver.find_element_by_id('input_password')
    password.send_keys("Www708626")
    url = "http://127.0.0.1:6000/b"
    files = {'image_file': ("captcha.jpg", open('C:\\Users\\Amor\\Downloads\\captcha.jpg', 'rb'), 'application')}
    r = requests.post(url=url, files=files)
    checkCode = json.loads(r.text)['value']
    checkCodeBox = driver.find_element_by_id('input_checkcode')
    checkCodeBox.send_keys(checkCode)
    loginButton = driver.find_element_by_id('loginButton')
    loginButton.click()
    time.sleep(5)


    #driver.quit()


if __name__ == '__main__':
    main()