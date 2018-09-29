# -*- coding: utf-8 -*-
# @Project : POM_demo 
# @Time    : 2018/9/3 14:22
# @Author  : 
# @File    : edu_mana_page.py
# @Software: PyCharm
from pages.basepage import BasePage

class EduMana(BasePage):
    '''运营管理后台-册次信息管理页面'''
    add_volume_button_xpath='//*[@id="app-content"]/edu-info/div/div/div/button'
    volume_name_xpath='//*[@id="app-content"]/edu-info/div/nz-modal/div/div[2]/div[1]/div/div[2]/div/form/div/div[1]/div/nz-input/input'
    volume_short_name_xpath='//*[@id="app-content"]/edu-info/div/nz-modal/div/div[2]/div[1]/div/div[2]/div/form/div/div[2]/div/nz-input/input'
    volume_sure_button_xpath='//*[@id="app-content"]/edu-info/div/nz-modal/div/div[2]/div[1]/div/div[3]/button[1]'
    def click_add_volume_button(self):
        '''点击 新增册次 按钮'''
        self.get_element_by_xpath(self.add_volume_button_xpath).click()

    def input_volume_name(self,volume_name):
        '''输入册次名称'''
        self.get_element_by_xpath(self.volume_name_xpath).send_keys(volume_name)

    def input_volume_short_name(self,short_name):
        '''输入册次简称'''
        self.get_element_by_xpath(self.volume_short_name_xpath).send_keys(short_name)

    def save_volume_info(self):
        '''输入完成后点击保存按钮'''
        self.get_element_by_xpath(self.volume_sure_button_xpath).click()
