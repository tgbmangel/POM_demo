# -*- coding: utf-8 -*-
# @Project : POM_demo 
# @Time    : 2018/5/30 15:25
# @Author  : 
# @File    : add_grade_class_page.py
# @Software: PyCharm Community Edition

from pages.basepage import BasePage


class SchoolAddGradeClass(BasePage):
    '''添加班级'''
    add_class_button_xpath='//*[@id="app-content"]/cla-info-mana-sm/div/div[2]/div/button[1]'
    class_no_id_xpath='/html/body/education-root/div/lay-out/nz-layout/nz-layout/nz-layout/nz-content/cla-info-mana-sm/div/nz-modal/div/div[2]/div[1]/div/div[2]/div/form/div[1]/div[1]/div/nz-input/input'
    class_name_xpath='/html/body/education-root/div/lay-out/nz-layout/nz-layout/nz-layout/nz-content/cla-info-mana-sm/div/nz-modal/div/div[2]/div[1]/div/div[2]/div/form/div[1]/div[2]/div/nz-input/input'
    class_year_xpath='/html/body/education-root/div/lay-out/nz-layout/nz-layout/nz-layout/nz-content/cla-info-mana-sm/div/nz-modal/div/div[2]/div[1]/div/div[2]/div/form/div[2]/div[1]/div/nz-input/input'
    class_grade_xpath='/html/body/education-root/div/lay-out/nz-layout/nz-layout/nz-layout/nz-content/cla-info-mana-sm/div/nz-modal/div/div[2]/div[1]/div/div[2]/div/form/div[2]/div[2]/div/nz-select/div/div/div[1]'
    class_grade_li_xpath='//*[@id="cdk-overlay-1"]/div/div/ul/li'
    class_room_xpath='/html/body/education-root/div/lay-out/nz-layout/nz-layout/nz-layout/nz-content/cla-info-mana-sm/div/nz-modal/div/div[2]/div[1]/div/div[2]/div/form/div[3]/div/div/nz-cascader/div/div/span'
    class_room_li_xpath='//*[@id="cdk-overlay-2"]/div/ul/li'
    class_room_li1_xpath='//*[@id="cdk-overlay-2"]/div/ul[2]/li'
    class_room_save_button_xpath='//*[@id="app-content"]/cla-info-mana-sm/div/nz-modal[1]/div/div[2]/div[1]/div/div[3]/button[1]'

    def click_add_class_grade(self):
        self.get_element_by_xpath(self.add_class_button_xpath).click()
        self.wait_time_second(1)
    def input_class_no_id(self,number):
        self.get_element_by_xpath(self.class_no_id_xpath).send_keys(number)
    def input_class_name(self,name):
        self.get_element_by_xpath(self.class_name_xpath).send_keys(name)
    def input_class_year(self,year):
        self.get_element_by_xpath(self.class_year_xpath).send_keys(year)
    def select_class_grade(self,index):
        self.get_select_element_by_xpath(self.class_grade_xpath,self.class_grade_li_xpath,index)
        self.wait_time_second(1)
    def select_class_room(self,build_index,room_index):
        self.get_select_element_by_xpath(self.class_room_xpath,self.class_room_li_xpath,build_index)
        self.wait_time_second(1)
        lis=self.driver.find_elements_by_xpath(self.class_room_li1_xpath)
        lis[room_index].click()
        self.wait_time_second(2)
        # self.mouse_move_and_click(1159, 427)
        self.brower_actions_esc()
    def save_class_add(self):
        self.get_element_by_xpath(self.class_room_save_button_xpath).click()