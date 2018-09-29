# -*- coding: utf-8 -*-
# @Project : POM_demo 
# @Time    : 2018/5/30 13:33
# @Author  : 
# @File    : add_building_page.py
# @Software: PyCharm Community Edition

from pages.basepage import BasePage
from time import sleep

class SchoolAddBuilding(BasePage):
    '''学校添加建筑页面'''
    build_add_button_xpath='/html/body/education-root/div/lay-out/nz-layout/nz-layout/nz-layout/nz-content/build-info-mana-sm/div/div/div/div[1]/button[1]'
    build_no_input_xpath='/html/body/education-root/div/lay-out/nz-layout/nz-layout/nz-layout/nz-content/build-info-mana-sm/div/nz-modal/div/div[2]/div[1]/div/div[2]/div/form/div[1]/div[1]/div/nz-input/input'
    build_name_input_xpath='/html/body/education-root/div/lay-out/nz-layout/nz-layout/nz-layout/nz-content/build-info-mana-sm/div/nz-modal/div/div[2]/div[1]/div/div[2]/div/form/div[1]/div[2]/div/nz-input/input'
    build_floors_xpath='/html/body/education-root/div/lay-out/nz-layout/nz-layout/nz-layout/nz-content/build-info-mana-sm/div/nz-modal/div/div[2]/div[1]/div/div[2]/div/form/div[2]/div[1]/div/nz-input/input'
    #
    build_use_type_xpath='/html/body/education-root/div/lay-out/nz-layout/nz-layout/nz-layout/nz-content/build-info-mana-sm/div/nz-modal/div/div[2]/div[1]/div/div[2]/div/form/div[2]/div[2]/div/nz-select/div/div/div[1]'
    build_use_type_li_xpath='//*[@id="cdk-overlay-1"]/div/div/ul/li'
    build_add_sure_button_xpath='//*[@id="app-content"]/build-info-mana-sm/div/nz-modal[1]/div/div[2]/div[1]/div/div[3]/button[1]'
    #教室
    manage_classroom_button_xpath='//*[@id="app-content"]/build-info-mana-sm/div/div/div/div[2]/nz-table/div/nz-spin/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[8]/a[3]'
    add_classroom_button_xpath='//*[@id="app-content"]/class-room/div/div/div/button[1]'
    classroom_no_xpath='/html/body/education-root/div/lay-out/nz-layout/nz-layout/nz-layout/nz-content/class-room/div/nz-modal/div/div[2]/div[1]/div/div[2]/div/form/div[1]/div[1]/div/nz-input/input'
    classroom_name_xpath='/html/body/education-root/div/lay-out/nz-layout/nz-layout/nz-layout/nz-content/class-room/div/nz-modal/div/div[2]/div[1]/div/div[2]/div/form/div[1]/div[2]/div/nz-input/input'
    classroom_type_xapth='//*[@id="app-content"]/class-room/div/nz-modal[1]/div/div[2]/div[1]/div/div[2]/div/form/div[2]/div[1]/div/nz-select/div/div/div[1]'
    classroom_type_drop_xpath='//*[@id="cdk-overlay-1"]/div/div/ul/li'
    classroom_floor_xpath='/html/body/education-root/div/lay-out/nz-layout/nz-layout/nz-layout/nz-content/class-room/div/nz-modal/div/div[2]/div[1]/div/div[2]/div/form/div[2]/div[2]/div/nz-input/input'
    classroom_save_button_xpath='//*[@id="app-content"]/class-room/div/nz-modal[1]/div/div[2]/div[1]/div/div[3]/button[1]'

    #
    def click_add_button(self):
        self.get_element_by_xpath(self.build_add_button_xpath).click()
        sleep(2)
    def input_build_no(self,number):
        self.get_element_by_xpath(self.build_no_input_xpath).send_keys(number)
    def input_build_name(self,build_name):
        self.get_element_by_xpath(self.build_name_input_xpath).send_keys(build_name)
    def input_build_floors(self,floors):
        self.get_element_by_xpath(self.build_floors_xpath).send_keys(floors)
    def input_build_use_type(self,index):
        self.get_select_element_by_xpath(self.build_use_type_xpath,self.build_use_type_li_xpath,index)
    def save_build_add(self):
        self.get_element_by_xpath(self.build_add_sure_button_xpath).click()
    #教室的:
    def click_manage_classroom_button(self):
        self.get_element_by_xpath(self.manage_classroom_button_xpath).click()
        sleep(2)
    def click_add_classroom_button(self):
        self.get_element_by_xpath(self.add_classroom_button_xpath).click()
        sleep(1)
    def input_classroom_no(self,number):
        self.get_element_by_xpath(self.classroom_no_xpath).send_keys(number)
    def input_classroom_name(self,name):
        self.get_element_by_xpath(self.classroom_name_xpath).send_keys(name)
    def select_classroom_type(self,indexer_select):
        self.get_select_element_by_xpath(self.classroom_type_xapth,self.classroom_type_drop_xpath,indexer_select)
    def input_classroom_floor(self,floor):
        self.get_element_by_xpath(self.classroom_floor_xpath).send_keys(floor)
    def save_classroom_add(self):
        self.get_element_by_xpath(self.classroom_save_button_xpath).click()