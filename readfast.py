#!usr/bin/python
# -*- coding: utf-8 -*-
# Author:Reg_coco
# www.qxn110.com
# Wechat: yikunzhu
from selenium import webdriver
import datetime
import time
import random
#创建浏览器对象
driver = webdriver.Chrome()
#窗口最大化显示
driver.maximize_window()

def login(url):
 
    driver.get(url)
    driver.implicitly_wait(10)
    time.sleep(2)

    driver.find_element_by_link_text("登录").click()
    
    print("请在30秒内完成登录！不能进行登录，请关闭本软件重新打开！")
    #用户扫码登陆
    time.sleep(30)
    
def dododo(dododo_time):
 

    r=random.randint(1,9)
    rr=r+1
    url11='https://wk3.bookan.com.cn/?id=21025&#/magazine/5994/webp-6/526247/'+str(rr)
    rr=rr+1
    url12='https://wk3.bookan.com.cn/?id=21025&#/magazine/5994/webp-6/526247/'+str(rr)
    rr=rr+1
    url13='https://wk3.bookan.com.cn/?id=21025&#/magazine/5994/webp-6/526247/'+str(rr)
    rr=rr+1
    url14='https://wk3.bookan.com.cn/?id=21025&#/magazine/5994/webp-6/526247/'+str(rr)
    rr=rr+1
    url15='https://wk3.bookan.com.cn/?id=21025&#/magazine/5994/webp-6/526247/'+str(rr)
    r=random.randint(1,3)
    rr=33968+r*2
    url21='https://wk3.bookan.com.cn/?id=21025#/listen/63818/part/'+str(rr)

    r=random.randint(1,9)
    rr=rr+1
    url31='https://wk3.bookan.com.cn/?id=21025&read3_good=2#/book/83692/epub-1/454605/Text|Section000'+str(rr)+'.xhtml'  #精选书籍1
    rr=rr+1
    url32='https://wk3.bookan.com.cn/?id=21025&read3_good=2#/book/83692/epub-1/454605/Text|Section000'+str(rr)+'.xhtml'  #精选书籍

    urlend='https://read3.bookan.com.cn/21025?#/task'


    btnplay='#app > div.routerWrap > div > div.listen-wrap > div.bot-wrap > div.botCtrl > div.btnCtrl > span.iconfont.ply'  #播放
    



    while True:
        try:
                    driver.get(url11)
                    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')+":正在进行阅读第1篇文章："+url11)
                    time.sleep(120)
                    driver.get(url12)
                    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')+":正在进行阅读第2篇文章："+url12)
                    time.sleep(120)
                    driver.get(url13)
                    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')+":正在进行阅读第3篇文章："+url13)
                    time.sleep(120)
                    driver.get(url14)
                    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')+":正在进行阅读第4篇文章："+url14)
                    time.sleep(120)
                    driver.get(url15)
                    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')+":正在进行阅读第5篇文章："+url15)
                    time.sleep(150)
                    driver.get(url21)
                    time.sleep(5)
                    driver.find_element_by_css_selector(btnplay).click()
                    time.sleep(5)
                    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')+":正在随机听课："+url21)
                    time.sleep(620)
                    driver.get(url31)
                    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')+":正在查看第1篇精选文章："+url31)
                    time.sleep(60)
                    driver.get(url32)
                    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')+":正在查看第2篇精选文章："+url32)
                    time.sleep(66)
                    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')+":你已完成本日任务！，正在为您跳转")
                    time.sleep(10)
                    driver.get(urlend)
                    time.sleep(6000)
                
        except:    
                    driver.get(url11)
                    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')+":正在进行阅读第1篇文章："+url11)
                    time.sleep(120)
                    driver.get(url12)
                    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')+":正在进行阅读第2篇文章："+url12)
                    time.sleep(120)
                    driver.get(url13)
                    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')+":正在进行阅读第3篇文章："+url13)
                    time.sleep(120)
                    driver.get(url14)
                    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')+":正在进行阅读第4篇文章："+url14)
                    time.sleep(120)
                    driver.get(url15)
                    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')+":正在进行阅读第5篇文章："+url15)
                    time.sleep(150)
                    driver.get(url21)
                    time.sleep(5)
                    driver.find_element_by_css_selector(btnplay).click()
                    time.sleep(5)
                    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')+":正在随机听课："+url21)
                    time.sleep(620)
                    driver.get(url31)
                    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')+":正在查看第1篇精选文章："+url31)
                    time.sleep(60)
                    driver.get(url32)
                    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')+":正在查看第2篇精选文章："+url32)
                    time.sleep(66)
                    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')+":你已完成本日任务！，正在为您跳转")
                    time.sleep(10)
                    driver.get(urlend)
                    time.sleep(6000)
 

 


if __name__ == "__main__":
 
    # bt = input("请输入开始时间【2019-02-15（空格）12:55:50】")
    url = "https://wk3.bookan.com.cn/?id=21025&#/personal/home"
    
    bt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f');
    login(url)
    dododo(bt)
