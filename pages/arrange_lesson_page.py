# -*- coding: utf-8 -*-
# @Project : POM_demo 
# @Time    : 2018/5/31 14:43
# @Author  : 
# @File    : arrange_lesson_page.py
# @Software: PyCharm Community Edition

from pages.basepage import BasePage
from time import sleep
from selenium.common.exceptions import NoSuchElementException
class ArrangeLesson(BasePage):
    '''备课组长安排'''
    drop_down_xpath='//div[@class="ant-select-selection__placeholder"]'
    drop_down_li_xpath='//li[@class="ant-select-dropdown-menu-item"]'
    save_button_xpath='//*[@id="app-content"]/teach-arrangement-lesson/div/div/nz-tabset/div/div/nz-tab-body/div[2]/button[1]'

    def select_drop_selection(self):
        drops=self.get_elements_by_xpath(self.drop_down_xpath)
        print('sss')
        for d in drops:
            if not d.is_displayed():
                print('sss')
            d.click()
            self.brower_actions_enter()
    def save_arrange_lesson(self):
        self.get_element_by_xpath(self.save_button_xpath).click()