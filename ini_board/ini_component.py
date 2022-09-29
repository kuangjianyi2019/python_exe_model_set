#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/9/3 10:46
# @Author : Yi Jian
# @File : ini_component.yaml.yaml.py
import tkinter
import typing
from tkinter import ttk
from typing import Dict
from typing import Union
from typing import Optional
from typing import Callable
from tkinter import *
from util.util import load_yaml


class IniComponent():

    dict_botton :Dict[str, Button]={}
    dict_radiobutton :Dict[str, Radiobutton]={}
    dict_frame : Dict[str, Frame]={}
    dict_labelframe : Dict[str, LabelFrame]={}
    dict_label: Dict[str, Label] = {}
    dict_combobox: Dict[str, ttk.Combobox] = {}
    dict_text : Dict[str, Text]={}
    dict_GLOBAL_VARIABLE : Dict[str, IntVar]={}

    def __init__(self):
        self.set_component()

    def botton(self):

        ini_button = Button()
        return ini_button

    def radiobutton(self):

        ini_radiobutton = Radiobutton()
        return ini_radiobutton

    def combobox(self):
        ini_combobox = ttk.Combobox()
        return ini_combobox

    def frame(self):
        ini_frame = Frame()
        return ini_frame

    def labelframe(self):

        ini_labelframe = LabelFrame()
        return ini_labelframe

    def text(self):
        ini_text = Text()
        return ini_text

    def scrollbar(self):
        ini_scrollbar = Scrollbar()
        return ini_scrollbar

    def ini_component(self, method_name, flag=1):
        if flag == 1:
            if hasattr(self, method_name):
                func = getattr(self, method_name)
                return func()
        else:
            if hasattr(self, 'dict_' + method_name):
                variable = getattr(self, 'dict_' + method_name)
                return variable

    def set_component(self):
        component_config = load_yaml('ini_component')
        for key, value in component_config.items():
            if value[0] != None:
                component = self.ini_component(key)
                component_dict = self.ini_component(key, flag=2)
                component_dict[key]=component

if __name__ == '__main__':
    ic = IniComponent()