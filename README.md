

<p align="center">
    <h1 align="center" >PhoneFuzz</h1>
    <p align="center">尝试枚举带*手机号</p>
        <p align="center">
    <a target="_blank" href="https://www.python.org/downloads/" title="Python version"><img src="https://img.shields.io/badge/python-%3E=_3.8+-green.svg"></a>
    <a target="_blank" href="LICENSE" title="License: MIT"><img src="https://img.shields.io/badge/License-MIT-blue.svg"></a>
    <a target="_blank" href="https://s045pd-phonefuzz-main-zewqvo.streamlit.app" title="Streamlit"><img src="https://static.streamlit.io/badges/streamlit_badge_black_white.svg"></a></p>
</p>


<img width="840" alt="image" src="https://github.com/s045pd/PhoneFuzz/assets/22721729/cc172904-7147-4cfe-ab93-5f7475f85e8d">

---
title: PhoneFuzz
emoji: 🕵️
colorFrom: pink
colorTo: green
sdk: streamlit
sdk_version: 1.22.0
app_file: main.py
pinned: false
---


## 🧑‍🦼 懒人使用

> 部署好的 streamlit 服务

[https://s045pd-phonefuzz-main-zewqvo.streamlit.app/](https://s045pd-phonefuzz-main-zewqvo.streamlit.app/)

## 🔧 环境安装

首先, 请确保您已经安装好 `python3.8+`, 然后运行如下命令.

```bash
git clone https://github.com/s045pd/PhoneFuzz.git

pip install -r requirements.txt
```

## 🏠 本地部署

### UI服务

启动web界面并开始使用

```bash
python -m streamlit run main.py
```

### 命令行

```bash
usage: main.py [-h] [-p PROVINCE] [-c CITY] [-t {移动,联通,电信,电信虚拟运营商,联通虚拟运营商,移动虚拟运营商}] [-z ZIP_CODE] [-d | --detail | --no-detail] phone

positional arguments:
  phone                 手机号模版

options:
  -h, --help            show this help message and exit
  -p PROVINCE, --province PROVINCE
                        省份
  -c CITY, --city CITY  城市
  -t {移动,联通,电信,电信虚拟运营商,联通虚拟运营商,移动虚拟运营商} --phone_type {移动,联通,电信,电信虚拟运营商,联通虚拟运营商,移动虚拟运营商}
                        运营商
  -z ZIP_CODE, --zip_code ZIP_CODE
                        邮编
  -d, --detail, --no-detail
                        输出详情
```


## 🤔️ Todo

思考中
