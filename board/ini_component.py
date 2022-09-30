#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/9/3 10:46
# @Author : Yi Jian
# @File : ini_component.yaml.yaml.py
import tkinter
import typing
from tkinter import ttk
from typing import Dict
from tkinter import *
from util.util import load_yaml
from board.component_func import ComponentFun

class IniComponent():
    dict_botton: Dict[str, Button] = {}
    dict_radiobutton: Dict[str, Radiobutton] = {}
    dict_frame: Dict[str, Frame] = {}
    dict_labelframe: Dict[str, LabelFrame] = {}
    dict_label: Dict[str, Label] = {}
    dict_combobox: Dict[str, ttk.Combobox] = {}
    dict_text: Dict[str, Text] = {}
    dict_scrollbar: Dict[str, Scrollbar] = {}
    dict_GLOBAL_VARIABLE: Dict[str, IntVar] = {}
    record_has_save_component = set()

    def __init__(self, tk: tkinter.Tk):
        self.tk = tk
        self.ct=ComponentFun(self.tk)
        self.component_yaml_config = load_yaml('ini_component')
        self.save_component_obj()
        self.set_component_config()

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

    def get_obj_property(self,obj,method_name, flag=1,*args):
        '''反射构建组件对象'''
        if flag == 1 :
            if hasattr(obj, method_name):

                obj_func = getattr(obj, method_name)
                return obj_func(*args)
        else:
            if hasattr(self, 'dict_' + method_name):
                obj_variable = getattr(self, 'dict_' + method_name)
                return obj_variable

    def save_component_obj(self):
        '''保存每一个组件'''
        for component_type, many_component_config in self.component_yaml_config.items():

            if many_component_config:

                for component_name in many_component_config:
                    component = self.get_obj_property(self,component_type)
                    component_variable = self.get_obj_property(self,component_type, flag=2)
                    self.record_has_save_component.add(component_type)
                    component_variable[component_name] = component

    def set_component_config(self):
        '''给组件设置属性'''
        for component_type in self.record_has_save_component:
            many_component_obj = self.get_obj_property(self,component_type, flag=2)
            many_component_config = self.component_yaml_config.get(component_type)

            # 获取已创建的组件dict
            for component_name, single_component_obj in many_component_obj.items():
                single_component_config = many_component_config.get(component_name)
                component_frame_parms = single_component_config.get('frame')
                component_text_parms = single_component_config.get('text')
                component_func_parms = single_component_config.get('func')
                component_pack_parms = single_component_config.get('pack')
                if component_frame_parms == 0:
                    single_component_obj.master = self.tk
                else:
                    # 获取对应的frame
                    frame_parms = component_frame_parms.split('-')
                    swap_many_component_obj = self.get_obj_property(self,frame_parms[0], flag=2)
                    single_component_obj.master = swap_many_component_obj.get(frame_parms[1])

                if component_text_parms:
                    single_component_obj.config(text=component_text_parms)

                if component_func_parms:
                    single_component_obj.config(command=lambda :self.get_obj_property(self.ct,component_func_parms))

                if component_pack_parms == 0:
                    single_component_obj.pack()


if __name__ == '__main__':
    ic = IniComponent(Tk())
    ic.tk.mainloop()
