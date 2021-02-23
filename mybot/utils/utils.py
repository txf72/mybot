from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time


import setting

url = setting.url
driver = webdriver.Chrome(setting.driver_path)


class find_func():

    def click(self, path):
        driver.find_element_by_xpath(path).click()
        time.sleep(2)
    
    def send_keys(self, path, word):
        driver.find_element_by_xpath(path).send_keys(word)
        time.sleep(2)



find_func = find_func()

class func():

    def login(self):
        driver.get(url)
        time.sleep(2)


        id_box = driver.find_element_by_name('username')
        pass_box = driver.find_element_by_name('password')
    

        id_box.send_keys(setting.username)
        pass_box.send_keys(setting.password)
        find_func.click(setting.login_button)


        find_func.click(setting.later_button)
        find_func.click(setting.off_button)


    def good(self):
        driver.get(url)
        time.sleep(2)

        tag = "アフィリエイト"
        find_func.send_keys(setting.tag_box, tag)
        find_func.click(setting.tag)


        target = driver.find_element_by_xpath(setting.target)
        actions = ActionChains(driver)
        actions.move_to_element(target)
        actions.perform()
        time.sleep(1)
        find_func.click(setting.post)

        num = 0
        while True:
            num += 1
            find_func.click(setting.good)
            find_func.click(setting.next) 
            if num < 200:
                continue
            else:
                break


