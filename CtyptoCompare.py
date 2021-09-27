from mylib import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
def login(driver):
    url = 'https://www.cryptocompare.com/coins/list/all/USD/1'
    driver.get(url)
    driver.implicitly_wait(3)
    driver.find_element_by_class_name('login-button').click()
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME,"email")))
    driver.find_element_by_name('email').send_keys('bobai@gmail.com')
    driver.find_element_by_name('password').send_keys('bobai123456')
    driver.find_element_by_xpath('//*[@id="pane-login"]/div/div[4]/div/button').click()

    return driver

if __name__=='__main__':
    driver = make_driver()
    driver = login(driver)
    rank,name,slug = [],[],[]
    for i in range(1,34):
        url = 'https://www.cryptocompare.com/coins/list/all/USD/' + str(i)
        driver.get(url)
        for j in range(2,102):
            try:
                trank = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div/div/coins-list-v2/div/div/table/tbody/tr[{}]/td[1]/div'.format(j)).text
                element = (driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div/div/coins-list-v2/div/div/table/tbody/tr[{}]/td[3]/a/h3/span[1]'.format(j)).text).split('\n')
                tname,tslug = element[0],element[1]
                rank.append(trank)
                name.append(tname)
                slug.append(tslug)
            except Exception as e:
                print(e)
                break

    data ={
        'rank' : rank,
        'name' : name,
        'slug' : slug
    }

    frame = pd.DataFrame(data)
    print(frame)
    frame.to_csv('CryptoCompare.csv',index=False)

                

    
            
    