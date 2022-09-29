#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/9/29 14:30
# @Author : Yi Jian
# @File : util.py
import os,sys
import yaml

curPath = os.path.abspath(os.path.dirname(__file__))
sys.path.append(curPath)
flie_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

def load_yaml(filename)->dict:
    '''加载yaml文件'''
    path = os.path.join(flie_path,f'{filename}.yaml')
    with open(path, mode='r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
        return data

if __name__ == '__main__':
    print(load_yaml('ini_component'))