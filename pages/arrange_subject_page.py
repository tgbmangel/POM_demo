# -*- coding: utf-8 -*-
# @Project : POM_demo 
# @Time    : 2018/5/31 11:28
# @Author  : 
# @File    : arrange_subject_page.py
# @Software: PyCharm Community Edition
from pages.basepage import BasePage

class ArrangeSubject(BasePage):
    # arrange_sub_save_button_xpath='/html/body/education-root/div/lay-out/nz-layout/nz-layout/nz-layout/nz-content/teach-arrangement-sub/div/div[2]/button[1]'
    arrange_sub_button_xpath='//*[@id="app-content"]/teach-arrangement-sub/div/div/div[2]/div[1]/div[1]/div/button'
    all_box='//*[@id="app-content"]/teach-arrangement-sub/nz-modal/div/div[2]/div[1]/div/div[2]/div/nz-transfer/nz-transfer-list[1]/div[1]/label/span/input'
    arrange_add_xpath='//*[@id="app-content"]/teach-arrangement-sub/nz-modal/div/div[2]/div[1]/div/div[2]/div/nz-transfer/div/button[2]'
    arrange_save_button_xpath='//*[@id="app-content"]/teach-arrangement-sub/nz-modal/div/div[2]/div[1]/div/div[3]/button[1]'

    def click_arrange_button(self):
        #点击第一个安排按钮
        self.get_element_by_xpath(self.arrange_sub_button_xpath).click()
    def select_all_box(self):
        self.get_element_by_xpath(self.all_box).click()
    def add_arrange(self):
        self.get_element_by_xpath(self.arrange_add_xpath).click()
    def save_arrange(self):
        self.get_element_by_xpath(self.arrange_save_button_xpath).click()