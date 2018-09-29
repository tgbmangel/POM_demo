# coding=utf-8

from pages.basepage import BasePage
from time import sleep

class TeacherInfoAddTeacher(BasePage):
    #添加非在编老师
    add_teacher_in_school_xpath='//*[@id="app-content"]/teach-info/div/div[2]/div/button[1]'
    #
    teacher_name_input_xpath='//*[@id="app-content"]/teach-add/div/form/div[1]/div[1]/div[1]/div/nz-input/input'
    # teacher_account_button_xpath='/html/body/education-root/div/lay-out/nz-layout/nz-layout/nz-layout/nz-content/teach-add/div/perfect-scrollbar/div/div[1]/div[1]/form/div[4]/div/button'
    # sex_input_xpath='/html/body/education-root/div/lay-out/nz-layout/nz-layout/nz-layout/nz-content/teach-add/div/perfect-scrollbar/div/div[1]/div[1]/form/div[5]/div/nz-select/div/div/div[1]'
    # sex_select_xpath='//*[@id="cdk-overlay-1"]/div/div/ul/li'
    # nation_xpath='/html/body/education-root/div/lay-out/nz-layout/nz-layout/nz-layout/nz-content/teach-add/div/perfect-scrollbar/div/div[1]/div[1]/form/div[7]/div/nz-input/input'
    id_number_xpath='//*[@id="app-content"]/teach-add/div/form/div[1]/div[1]/div[2]/div/nz-input/input'
    # jiguan_xpath='/html/body/education-root/div/lay-out/nz-layout/nz-layout/nz-layout/nz-content/teach-add/div/perfect-scrollbar/div/div[1]/div[1]/form/div[9]/div/nz-input/input'
    # address_xpath='/html/body/education-root/div/lay-out/nz-layout/nz-layout/nz-layout/nz-content/teach-add/div/perfect-scrollbar/div/div[1]/div[1]/form/div[10]/div/nz-input/input'
    # address_now_xpath='/html/body/education-root/div/lay-out/nz-layout/nz-layout/nz-layout/nz-content/teach-add/div/perfect-scrollbar/div/div[1]/div[1]/form/div[11]/div/nz-input/input'
    # birth_day_xpath='/html/body/education-root/div/lay-out/nz-layout/nz-layout/nz-layout/nz-content/teach-add/div/perfect-scrollbar/div/div[1]/div[1]/form/div[18]/div/nz-datepicker/span/input'
    # birthday_class='ant-calendar-picker-input ant-input'
    # birth_day_index=1
    phone_xpath='//*[@id="app-content"]/teach-add/div/form/div[1]/div[1]/div[4]/div/nz-input/input'
    nation_xpath='//*[@id="app-content"]/teach-add/div/form/div[1]/div[1]/div[7]/div/nz-select/div/div/div[1]'
    nation_drop_xpath='//*[@id="cdk-overlay-1"]/div/div/ul/li'
    zhengzhimianmao_xpath='//*[@id="app-content"]/teach-add/div/form/div[1]/div[1]/div[8]/div/nz-select/div/div/div[1]'
    zhengzhimianmao_drop_xpath='//*[@id="cdk-overlay-2"]/div/div/ul/li'
    zhicheng_xpath='//*[@id="app-content"]/teach-add/div/form/div[2]/div/nz-select/div/div/div[1]'
    zhicheng_drop_xpath='//*[@id="cdk-overlay-3"]/div/div/ul/li'
    # image_xpath='/html/body/education-root/div/lay-out/nz-layout/nz-layout/nz-layout/nz-content/teach-add/div/perfect-scrollbar/div/div[1]/div[2]/div[1]/div/nz-upload-file/div/nz-upload/div/div/input'
    save_xpath='//*[@id="app-content"]/teach-add/div/div/button[1]'
    #添加完成后，回到列表页
    partment_arrange_button_xpath='//*[@id="app-content"]/teach-info/div/div[2]/nz-table/div/nz-spin/div[2]/div/div/div/div/div/table/tbody/tr/td[11]/a[3]'
    check_box_xpath='//input[@type="checkbox"]'
    partment_arrange_save_button_xpath='//*[@id="app-content"]/teach-info/div/nz-modal[2]/div/div[2]/div[1]/div/div[3]/button[1]'
    arrange_success_link_text= u'教师安排部门成功'
    #
    def add_teacher_in_scholl_button_click(self):
        self.get_element_by_xpath(self.add_teacher_in_school_xpath).click()
    def input_teacher_name(self,names):
        self.get_element_by_xpath(self.teacher_name_input_xpath).send_keys(names)
    def input_teacher_id(self,id_number):
        self.get_element_by_xpath(self.id_number_xpath).send_keys(id_number)
    def input_teacher_phone(self,phone):
        self.get_element_by_xpath(self.phone_xpath).send_keys(phone)
    def select_teacher_nation(self,indxer_select):
        self.get_select_element_by_xpath(self.nation_xpath,self.nation_drop_xpath,indxer_select)
    def select_teacher_zhizhengmianmao(self,indxer_select):
        self.get_select_element_by_xpath(self.zhengzhimianmao_xpath,self.zhengzhimianmao_drop_xpath,indxer_select)
    def select_teacher_zhicheng(self,indxer_select):
        self.get_select_element_by_xpath(self.zhicheng_xpath,self.zhicheng_drop_xpath,indxer_select)
    def save_teacher_info(self):
        self.browser_action_scroll_dwon()
        self.get_element_by_xpath(self.save_xpath).click()
    #部门安排
    def click_partment_arrange(self):
        self.get_element_by_xpath(self.partment_arrange_button_xpath).click()
        self.wait_time_second(2)
    def check_all_box(self):
        check_boxes=self.get_elements_by_xpath(self.check_box_xpath)
        for x in check_boxes[6:]:
            #现在前6个是默认的一些机构。过滤掉
            if not x.is_selected():
                self.browser_scroll_to_element(x)
                x.click()
        self.wait_time_second(1)
    def save_partment_arrange(self):
        self.get_element_by_xpath(self.partment_arrange_save_button_xpath).click()
