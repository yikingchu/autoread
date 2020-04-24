#!usr/bin/python
# -*- coding: utf-8 -*-
# Author:Reg_coco
# www.qxn110.com
# Wechat: yikunzhu
from selenium import webdriver
import datetime
import time

#创建浏览器对象
driver = webdriver.Chrome()
#窗口最大化显示
driver.maximize_window()

def login(url):
 
    driver.get(url)
    driver.implicitly_wait(10)
    time.sleep(2)

    driver.find_element_by_link_text("登录").click()
    
    print("请在30秒内完成登录")
    #用户扫码登陆
    time.sleep(2)
    
def buy(buy_time):
 
    url2='https://wk3.bookan.com.cn/?id=21025#/'
    btn1='#footerBar > div.weui-tabbar > a.weui-tabbar__item.readRank'  #读书榜
       

    btn4='#contentWrap > dl:nth-child(4) > dd > a:nth-child(1) > div > img'  #热门期刊第二篇

    btn5='#twrap'  #读内容

    btn8='#twrap'  #下一页
    url4='https://wk3.bookan.com.cn/?id=21025#/audio/828'
    
    btn6='#booksList > a:nth-child(1) > div > img'  #点击热门听书

    btn7='#app > div.routerWrap > div > div.listen-wrap > div.bot-wrap > div.botCtrl > div.btnCtrl > span.iconfont.ply'  #播放
    

    url3='https://read3.bookan.com.cn/21025?#/read'  #精选书籍
    btn9='#root > div > div.pageWrap > div > div.list > div:nth-child(1) > img'   #精选书籍


   



    while True:
        try:
                    driver.find_element_by_css_selector(btn4).click()
                    time.sleep(0.5)
                    driver.find_element_by_css_selector(btn5).click()
                    time.sleep(5)
                    driver.find_element_by_css_selector(btn8).click()
                    time.sleep(60)
                    driver.find_element_by_css_selector(btn8).click()
                    time.sleep(60)
                    driver.find_element_by_css_selector(btn8).click()
                    time.sleep(60)
                    driver.find_element_by_css_selector(btn8).click()
                    time.sleep(60)
                    driver.find_element_by_css_selector(btn8).click()
                    time.sleep(60)
                    driver.find_element_by_css_selector(btn8).click()
                    time.sleep(60)
                    driver.find_element_by_css_selector(btn8).click()
                    time.sleep(60)
                    driver.find_element_by_css_selector(btn8).click()
                    time.sleep(60)
                    driver.find_element_by_css_selector(btn8).click()
                    time.sleep(60)
                    driver.get(url4)
                    driver.find_element_by_css_selector(btn6).click()
                    time.sleep(0.5)
                    driver.find_element_by_css_selector(btn7).click()
                    time.sleep(620)
                    driver.get(url3)
                    driver.find_element_by_css_selector(btn9).click()
                    time.sleep(60)
                    driver.find_element_by_css_selector(btn8).click()
                    time.sleep(600)
                    print("完成刷分")
                
        except:
                    driver.get(url4)
                    driver.find_element_by_css_selector(btn6).click()
                    time.sleep(0.5)
                    driver.find_element_by_css_selector(btn7).click()
                    time.sleep(620)
                    driver.get(url3)
                    driver.find_element_by_css_selector(btn9).click()
                    time.sleep(600)
                    driver.get(url)
                    driver.find_element_by_css_selector(btn5).click()
                    time.sleep(5)
                    driver.find_element_by_css_selector(btn8).click()
                    time.sleep(60)
                    driver.find_element_by_css_selector(btn8).click()
                    time.sleep(60)
                    driver.find_element_by_css_selector(btn8).click()
                    time.sleep(60)
                    driver.find_element_by_css_selector(btn8).click()
                    time.sleep(60)
                    driver.find_element_by_css_selector(btn8).click()
                    time.sleep(60)
                    driver.find_element_by_css_selector(btn8).click()
                    time.sleep(60)
                    driver.find_element_by_css_selector(btn8).click()
                    time.sleep(60)
                    driver.find_element_by_css_selector(btn8).click()
                    time.sleep(60)
                    driver.find_element_by_css_selector(btn8).click()
                    time.sleep(60)
                    driver.get(url2)
                    driver.find_element_by_css_selector(btn6).click()
                    time.sleep(0.5)
                    driver.find_element_by_css_selector(btn7).click()
                    time.sleep(620)
                    driver.get(url3)
                    driver.find_element_by_css_selector(btn9).click()
                    time.sleep(60)
                    driver.find_element_by_css_selector(btn8).click()
                    time.sleep(600)
                    print("完成刷分")
 

 


if __name__ == "__main__":
 
    # bt = input("请输入开始时间【2019-02-15（空格）12:55:50】")
    url = "https://wk3.bookan.com.cn/?id=21025&#/personal/home"
    
    bt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f');
    login(url)
    buy(bt)
