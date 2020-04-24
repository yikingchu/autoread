# 软件名称：自动读书 （AutoRead）
## 作用：自动阅读、自动听书，博看群书书苑、民航读书工会读书，适合自动学习等。仅供探究，不可用于其他用途。
Author:Reg_coco 
Wechat:yikunzhu

### CENTOS:
yum install -y  python36
yum install -y python36-setuptools
yum install -y python36-pip
pip --default-timeout=100 install selenium #国内镜像：pip install --index https://mirrors.ustc.edu.cn/pypi/web/simple/  selenium

### DEBIAN/UBUNTU:
sudo apt-get update
sudo apt-get install python3.6
pip --default-timeout=100 install selenium #国内镜像：pip install --index https://mirrors.ustc.edu.cn/pypi/web/simple/  selenium

### WINDOWS:
 安装python3
 安装pip
 pip --default-timeout=100 install selenium #国内镜像：pip install --index https://mirrors.ustc.edu.cn/pypi/web/simple/  selenium

## 使用说明：
Python read.py

根据测试，输入信息即可。

现目前适配 chrome81版本。
