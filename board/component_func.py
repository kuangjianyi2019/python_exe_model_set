#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/9/30 15:35
# @Author : Yi Jian
# @File : component_func.py
import os,sys
import tkinter.messagebox as msb
curPath = os.path.abspath(os.path.dirname(__file__))
sys.path.append(curPath)

class ComponentFun():

    def __init__(self,tk):
      self.tk=tk

    def message_box(self):
        msb.showinfo('很强')


