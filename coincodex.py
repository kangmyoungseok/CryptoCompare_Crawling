from mylib import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from selenium.webdriver import ActionChains
import time


def login(driver):
    url = 'https://coincodex.com/'
    driver.get(url)
    driver.implicitly_wait(3)
    driver.find_element_by_xpath('//*[@id="navbar"]/div[1]/header-user/div/ul/li[6]/span').click()
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,"modal-auth")))
    driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/ngbd-modal-content/div/div[2]/form/input[1]').send_keys('kms01297@gmail.com')
    driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/ngbd-modal-content/div/div[2]/form/input[2]').send_keys('bobai123456')
    driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/ngbd-modal-content/div/div[2]/form/button').click()
    driver.find_element_by_class_name('login-button').click()

    return driver


if __name__=='__main__':
    driver = make_driver()
    driver = login(driver)
    driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/ngbd-modal-content/div/i').click() #광고1 닫기
    time.sleep(5)
    driver.find_element_by_id('CCx5StickyBottom').find_element_by_class_name("close").click()
    some_tag = driver.find_element_by_xpath('//*[@id="table-container"]/div/div[3]/a')
    action = ActionChains(driver)
    while 1:
        try:
            action.move_to_element(some_tag).perform() #스크롤 아래로 내리고
            driver.find_element_by_xpath('//*[@id="table-container"]/div/div[3]/a').click() # 더보기 클릭
            time.sleep(2)
        except:
            break
    
    ranks = driver.find_elements_by_class_name('rank')
    name = driver.find_elements_by_class_name('name')
    
    
    driver.quit()


