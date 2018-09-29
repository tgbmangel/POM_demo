# -*- coding: utf-8 -*-
# @Project : POM_demo 
# @Time    : 2018/5/31 10:06
# @Author  : 
# @File    : add_orgnize_page.py
# @Software: PyCharm Community Edition

from pages.basepage import BasePage

class SchoolAddOrg(BasePage):
    '''学校添加机构组织'''
    # add_org_button_xpath='/html/body/education-root/div/lay-out/nz-layout/nz-layout/nz-layout/nz-content/organ-info-mana-sm/div/div[1]/div/a[1]'
    add_org_button_xpath='/html/body/education-root/div/lay-out/nz-layout/nz-layout/nz-layout/nz-content/organ-info-mana-sm/div/div[1]/div/div/button[1]'
    org_type_xpath='/html/body/education-root/div/lay-out/nz-layout/nz-layout/nz-layout/nz-content/organ-info-mana-sm/div/nz-modal[1]/div/div[2]/div[1]/div/div[2]/div/form/div[1]/div[2]/div/nz-select/div/div/div[1]'
    org_type_li_xpath='//*[@id="cdk-overlay-1"]/div/div/ul/li'

    org_name_xpath='/html/body/education-root/div/lay-out/nz-layout/nz-layout/nz-layout/nz-content/organ-info-mana-sm/div/nz-modal[1]/div/div[2]/div[1]/div/div[2]/div/form/div[2]/div/div/nz-select/div/div/div[1]'
    org_name_li_xpath='//*[@id="cdk-overlay-2"]/div/div/ul/li'
    org_save_button_xpath='/html/body/education-root/div/lay-out/nz-layout/nz-layout/nz-layout/nz-content/organ-info-mana-sm/div/nz-modal[1]/div/div[2]/div[1]/div/div[3]/button[2]'
    #
    org_next_xpath='/html/body/education-root/div/lay-out/nz-layout/nz-layout/nz-layout/nz-content/organ-info-mana-sm/div/div[1]/perfect-scrollbar/div/div[1]/nz-spin/div[2]/div/tree-root/tree-viewport/div/div/tree-node-collection/div/tree-node/div/tree-node-children/div/tree-node-collection/div/tree-node/div/tree-node-wrapper/div/div'
    org_next_type_xpath='/html/body/education-root/div/lay-out/nz-layout/nz-layout/nz-layout/nz-content/organ-info-mana-sm/div/nz-modal[1]/div/div[2]/div[1]/div/div[2]/div/form/div[1]/div[2]/div/nz-select/div/div/div[1]'
    org_next_type_li_xpath='//*[@id="cdk-overlay-1"]/div/div/ul/li'
    org_next_name_xpath='/html/body/education-root/div/lay-out/nz-layout/nz-layout/nz-layout/nz-content/organ-info-mana-sm/div/nz-modal[1]/div/div[2]/div[1]/div/div[2]/div/form/div[2]/div/div/nz-select/div/div/div[1]'
    org_next_name_li_xpath='//*[@id="cdk-overlay-3"]/div/div/ul/li'
    org_next_save_button_xpath='/html/body/education-root/div/lay-out/nz-layout/nz-layout/nz-layout/nz-content/organ-info-mana-sm/div/nz-modal[1]/div/div[2]/div[1]/div/div[3]/button[2]'
    #
    def click_add_org(self):
        self.get_element_by_xpath(self.add_org_button_xpath).click()
        self.wait_time_second(1)
    def select_org_type(self,index):
        self.get_select_element_by_xpath(self.org_type_xpath,self.org_type_li_xpath,index)
    def select_org_name(self,index):
        self.get_select_element_by_xpath(self.org_name_xpath,self.org_name_li_xpath,index)
    def save_add_org(self):
        self.get_element_by_xpath(self.org_save_button_xpath).click()
    #

    def select_org_next(self):
        self.get_element_by_xpath(self.org_next_xpath).click()
    def select_org_next_type(self,index):
        self.get_select_element_by_xpath(self.org_next_type_xpath,self.org_next_type_li_xpath,index)
        self.wait_time_second(1)
    def select_org_next_name(self,index):
        self.get_select_element_by_xpath(self.org_next_name_xpath,self.org_next_name_li_xpath,index)
        self.wait_time_second(1)
    def save_next_add_org(self):
        self.get_element_by_xpath(self.org_next_save_button_xpath).click()