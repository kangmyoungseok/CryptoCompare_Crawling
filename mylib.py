import requests
from selenium import webdriver
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support import expected_conditions as EC
#from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
#from bs4 import BeautifulSoup
import pandas as pd
import glob
import os

from multiprocessing import Pool
import multiprocessing as mp



def make_options():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
#    chrome_options.add_experimental_option( "prefs",{'profile.managed_default_content_settings.javascript': 2})
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_argument('disable-gpu')
#    chrome_options.add_argument('--headless')
    chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.67 Safari/537.36')
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument('--ignore-certificate-errors-spki-list')
    chrome_options.add_argument("--ignore-ssl-errors")
    chrome_options.add_argument("--ignore-certificate-error")
    chrome_options.add_argument("start-maximized") 
    chrome_options.add_argument("disable-infobars") 
    chrome_options.add_argument("--disable-extensions") 
   
    return chrome_options

#Chrome Driver 생성
def make_driver():
    chrome_options = make_options()
    driver = webdriver.Chrome(executable_path = './chromedriver.exe',options = chrome_options)   
    return driver


def replace_url(prefix, url):
    url = url.split(',')
    url[0] = url[0].replace("[", "")
    url[0] = url[0].replace("https://", "")
    url[0] = url[0].replace("http://", "")
    url[0] = url[0].replace("www.", "")
    url[0] = url[0].replace("]", "")
    url = url[0].replace("'", "")
    url = prefix + url
    return url

def split_csv(total_csv):
    rows = pd.read_csv(total_csv,chunksize=50)
    file_count = 0
    for i, chuck in enumerate(rows):
        chuck.to_csv('out{}.csv'.format(i))
        file_count = file_count+1
    return file_count

def merge_csv():
    input_file = r'/result' # csv파일들이 있는 디렉토리 위치
    output_file = r'/result/total.csv' # 병합하고 저장하려는 파일명

    allFile_list = glob.glob(os.path.join(input_file, 'fout*')) # glob함수로 fout로 시작하는 파일들을 모은다
    print(allFile_list)
    allData = [] # 읽어 들인 csv파일 내용을 저장할 빈 리스트를 하나 만든다
    for file in allFile_list:
        df = pd.read_csv(file) # for구문으로 csv파일들을 읽어 들인다
        allData.append(df) # 빈 리스트에 읽어 들인 내용을 추가한다

    dataCombine = pd.concat(allData, axis=0, ignore_index=True) # concat함수를 이용해서 리스트의 내용을 병합
    # axis=0은 수직으로 병합함. axis=1은 수평. ignore_index=True는 인데스 값이 기존 순서를 무시하고 순서대로 정렬되도록 한다.
    dataCombine.to_csv(output_file, index=False) # to_csv함수로 저장한다. 인데스를 빼려면 False로 설정


#main template
'''
    if __name__=='__main__':
        total_csv = pd.read_csv('total_v1.1.csv')
        file_count = split_csv(total_csv)
        
        for i in range(file_count):
            file_name = 'out{}.csv'.format(i)
            data = pd.read_csv(file_name,encoding ='CP949')
            data = data.to_dict('records')
            try:
                pool = Pool(processes=6)
                result = pool.map(get_deadlink,data)
                print("------------------------------------------")
                print(file_name + " is completed")
                print("-------------------------------------------")

                for i in range(len(data)):
                    data[i]['dead_link_ratio'] = result[i]
                list_df = pd.DataFrame(data)
                list_df.to_csv(file_name,index=False)
            except Exception as e:
                print(e)
'''