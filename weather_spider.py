# 分析请求页面数据和url
import time

import requests # 模拟浏览器进行网络请求
from lxml import etree # 进行数据预处理
import csv # 写入csv文件
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def getWeather(url):
    # 创建Chrome选项
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # 无头模式，不显示窗口
    chrome_options.add_argument('--no-sandbox')  # 解决某些Linux环境下的问题
    chrome_options.add_argument('--disable-dev-shm-usage')  # 防止内存不足问题
    # 打开谷歌浏览器,点击'查看更多'按钮
    driver=webdriver.Chrome(options=chrome_options)
    driver.get (url)

    button=driver.find_element(By.CLASS_NAME,'lishidesc2')
    button.click()
    #等待页面加载
    time.sleep(3)
    # 新建一个列表,将爬取每月数据放进去
    weather_info=[]
    # 请求头信息:浏览器版本型号,接收数据的编码格式
    # 模拟浏览器,发送网络请求,防止反爬
    # headers={
    #     # 必填,不填拿不到数据
    #     'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) '
    #                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 '
    #                  'Mobile Safari/537.36'
    # }
    # # 请求
    # resp=requests.get(url,headers=headers)
    # # 数据预处理
    # resp_html=etree.HTML(resp.text)
    # 用Selenium获取点击后的页面源码
    page_source=driver.page_source
    # 用lxml解析Selenium获取的页面源码
    resp_html=etree.HTML(page_source)
    print(resp_html)
    # xpath提取所有数据
    resp_list=resp_html.xpath("//ul[@class='thrui']/li")
    print(resp_list)
    # for循环遍历
    for li in resp_list:
        # 每天的数据存放到一个字典里
        day_weather_info={}
        # 日期 日期格式是 2029-12-12 星期二,但是我们不需要星期二
        day_weather_info['日期']=li.xpath("./div[1]/text()")[0].split(' ')[0]
        #最高气温(包含摄氏度符号)
        high_temp=li.xpath("./div[2]/text()")[0]
        day_weather_info['最高气温']=high_temp[:high_temp.find('℃')]
        #最低气温
        low_temp=li.xpath("./div[3]/text()")[0]
        day_weather_info['最低气温']=low_temp[:low_temp.find('℃')]
        #天气
        day_weather_info['天气']=li.xpath("./div[4]/text()")[0]
        #风向
        day_weather_info['风向']=li.xpath("./div[5]/text()")[0]
        weather_info.append(day_weather_info)
    return weather_info

year_weather=[]
# 循环获取2025一年的天气
for i in range(1,13):

    month='0'+str(i) if i<10 else str(i)
    url='https://lishi.tianqi.com/huzhou/2025'+month+'.html'
    month_weather=getWeather(url)
    print(month_weather)
    year_weather.append(month_weather)

print(year_weather)

# 数据写入
# Windows系统中，Python在写入文本文件时会自动将 \n 转换为 \r\n（回车+换行），
# 而CSV模块已经处理了换行，导致双重换行。
with open('湖州2025年天气数据.csv','w',newline='',encoding='utf-8') as csvfile:
    writer=csv.writer(csvfile)
    #先写入列名
    writer.writerow(['日期','最高气温','最低气温','天气','风向'])
    #一次写入多行用writerows(写入的数据类型是列表,一个列表代表一行)
    list_year=[]
    for month_weather in year_weather:
        for day_weather_dict in month_weather:
            list_year.append(list(day_weather_dict.values()))
    writer.writerows(list_year)

