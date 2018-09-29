# coding=utf-8
from selenium.webdriver.common.by import By
from pages.basepage import BasePage
from time import sleep

class SchoolInfoManageAddPag(BasePage):
    '''教育局管理后台-学校信息管理页面'''
    scho_name_input_xpath='//*[@id="app-content"]/scho-add/div/form/div[1]/div[1]/div[1]/div/nz-input/input'
    # scho_name_chin_xpath='/html/body/education-root/div/lay-out/nz-layout/nz-layout/nz-layout/nz-content/scho-add/div/perfect-scrollbar/div/div[1]/div[1]/form/div[2]/div/nz-input/input'
    # scho_name_eng_xpath='/html/body/education-root/div/lay-out/nz-layout/nz-layout/nz-layout/nz-content/scho-add/div/perfect-scrollbar/div/div[1]/div[1]/form/div[3]/div/nz-input/input'
    # scho_name_eng_s_xpath='/html/body/education-root/div/lay-out/nz-layout/nz-layout/nz-layout/nz-content/scho-add/div/perfect-scrollbar/div/div[1]/div[1]/form/div[4]/div/nz-input/input'
    scho_code_xpath='//*[@id="app-content"]/scho-add/div/form/div[1]/div[1]/div[5]/div/nz-input/input'
    # class_of_school_xpath = '/html/body/education-root/div/lay-out/nz-layout/nz-layout/nz-layout/nz-content/scho-add/div/perfect-scrollbar/div/div[1]/div[1]/form/div[6]/div/nz-select/div/div/div[1]'
    # class_of_school_drop_xpath = '//*[@id="cdk-overlay-1"]/div/div/ul/li'
    #学区
    scho_dis_xpath='//*[@id="app-content"]/scho-add/div/form/div[1]/div[1]/div[6]/div/nz-select/div/div/div[1]'
    scho_dis_drop_xpath='//*[@id="cdk-overlay-1"]/div/div/ul/li'
    #学校类别
    scho_temp_xpath='//*[@id="app-content"]/scho-add/div/form/div[1]/div[1]/div[7]/div/nz-select/div/div/div[1]'
    scho_temp_drop_xpath='//*[@id="cdk-overlay-2"]/div/div/ul/li'
    #办学类别
    scho_type_xpath='//*[@id="app-content"]/scho-add/div/form/div[1]/div[1]/div[8]/div/nz-select/div/div/div[1]'
    scho_type_drop_xpath='//*[@id="cdk-overlay-3"]/div/div/ul/li'
    # scho_location_xpath='/html/body/education-root/div/lay-out/nz-layout/nz-layout/nz-layout/nz-content/scho-add/div/perfect-scrollbar/div/div[1]/div[1]/form/div[9]/div/nz-cascader/div/div/span'
    # scho_location_drop_xpath='//*[@id="cdk-overlay-4"]/div/ul/li'
    # scho_location_input_xpath='/html/body/education-root/div/lay-out/nz-layout/nz-layout/nz-layout/nz-content/scho-info/div/scho-add/div/nz-spin/div[2]/perfect-scrollbar/div/div[1]/div[1]/form/div[9]/div/nz-cascader/div/div/input'
    # scho_detail_location_xpath='/html/body/education-root/div/lay-out/nz-layout/nz-layout/nz-layout/nz-content/scho-add/div/perfect-scrollbar/div/div[1]/div[1]/form/div[10]/div/nz-input/input'
    school_master_xpath='//*[@id="app-content"]/scho-add/div/form/div[4]/div/nz-input/input'
    # scho_create_time_input_xpath='/html/body/education-root/div/lay-out/nz-layout/nz-layout/nz-layout/nz-content/scho-add/div/perfect-scrollbar/div/div[1]/div[1]/form/div[13]/div/nz-datepicker/span/input'
    # upload_image_button_xpath = '/html/body/education-root/div/lay-out/nz-layout/nz-layout/nz-layout/nz-content/scho-add/div/perfect-scrollbar/div/div[1]/div[2]/div[1]/div/nz-upload-file/div/nz-upload/div/div/input'
    #upload_image_button_xpath = '/html/body/education-root/div/lay-out/nz-layout/nz-layout/nz-layout/nz-content/scho-info/div/scho-add/div/nz-spin/div[2]/perfect-scrollbar/div/div[1]/div[2]/div[1]/div/nz-upload-file/div/div/nz-upload/div/div/input'
    scho_add_save_button_xpath='//*[@id="app-content"]/scho-add/div/div/button[1]'
    #
    success_message_xpath='/html/body/education-root/div/lay-out/nz-layout/nz-layout/nz-layout/nz-content/scho-add/div/nz-modal[2]/div/div[2]/div[1]/div/div[2]/div/p'
    sure_button_xpath='/html/body/education-root/div/lay-out/nz-layout/nz-layout/nz-layout/nz-content/scho-add/div/nz-modal[2]/div/div[2]/div[1]/div/div[3]/button[2]'
    role_all_select_xpath='/html/body/education-root/div/lay-out/nz-layout/nz-layout/nz-layout/nz-content/scho-add/div/nz-modal[1]/div/div[2]/div[1]/div/div[2]/div/perfect-scrollbar/div/div[1]/div/div[1]/label/span[2]'
    role_sure_xpath='/html/body/education-root/div/lay-out/nz-layout/nz-layout/nz-layout/nz-content/scho-add/div/nz-modal[1]/div/div[2]/div[1]/div/div[3]/button[2]'

    #yuansu
    def open(self):
        self._open(self.base_url, self.pagetitle)
        sleep(3)
    #控件
    def input_scho_name(self,scho_name):
        self.get_element_by_xpath(self.scho_name_input_xpath).send_keys(scho_name)
    # def input_scho_chin_name(self,scho_chin_name):
    #     self.find_element(*self.scho_name_chin_loc).send_keys(scho_chin_name)
    # def input_scho_eng_name(self,scho_eng_name):
    #     self.find_element(*self.scho_name_eng_loc).send_keys(scho_eng_name)
    # def input_scho_eng_s_name(self,scho_eng_s_name):
    #     self.find_element(*self.scho_name_eng_s_loc).send_keys(scho_eng_s_name)
    def input_scho_code(self,scho_code):
        self.get_element_by_xpath(self.scho_code_xpath).send_keys(scho_code)
    ##下拉控件
    ##还未做：共有多少个下拉选项进行限制
    # def school_class_drop_select(self,indexer_select):
    #     self.find_element(*self.class_of_school_element_loc).click()
    #     lis=self.driver.find_elements_by_xpath(self.class_of_school_drop_xpath)
    #     lis[indexer_select].click()
    def school_dis_drop_select(self,indexer_select):
        self.get_select_element_by_xpath(self.scho_dis_xpath,self.scho_dis_drop_xpath,indexer_select)

    def school_temp_drop_select(self,indexer_select):
        self.get_select_element_by_xpath(self.scho_temp_xpath,self.scho_temp_drop_xpath,indexer_select)
        sleep(0.5)
        self.brower_actions_esc()
    def school_type_drop_select(self,indexer_select):
        self.get_select_element_by_xpath(self.scho_type_xpath,self.scho_type_drop_xpath,indexer_select)
    # def school_location_select(self,indexer_select):
    #     self.driver.find_element_by_xpath(self.scho_location_xpath).click()
    #     sleep(1)
    #     lis=self.driver.find_elements_by_xpath(self.scho_location_drop_xpath)
    #     lis[indexer_select].click()
    #     sleep(2)
    #输入控件
    # def input_detail_location(self, detail_location):
    #     self.find_element(*self.scho_detail_location_loc).send_keys(detail_location)
    def input_scho_master(self, scho_master_name):
        self.get_element_by_xpath(self.school_master_xpath).send_keys(scho_master_name)
    # def input_scho_create_time(self,time_input):
    #     js = "var list=document.getElementsByClassName(\"ant-calendar-picker-input ant-input\");list[0].removeAttribute('readonly');"
    #     self.script(js)
    #     self.find_element(*self.scho_create_time_input_loc).send_keys(time_input)
    # def upload_image(self,image_path):
    #     self.driver.find_element_by_xpath(self.upload_image_button_xpath).send_keys(image_path)
    def save_info_click(self):
        # self.browser_action_scroll_dwon()
        save_button=self.get_element_by_xpath(self.scho_add_save_button_xpath)
        self.browser_scroll_to_element(save_button)
        save_button.click()
    #判定方法
    def success_info(self):
        info=self.get_element_by_xpath(self.success_message_xpath)
        sure_button=self.get_element_by_xpath(self.sure_button_xpath)
        try:
            sure_button.click()
            sleep(5)
            self.get_element_by_xpath(self.role_all_select_xpath).click()
            self.get_element_by_xpath(self.role_sure_xpath).click()
            return True
        except Exception as e:
            return False

    def save_button_enable(self):
        button=self.driver.find_element_by_xpath(self.scho_add_save_button_xpath)
        if button.is_enabled():
            return True
        else:
            return False

