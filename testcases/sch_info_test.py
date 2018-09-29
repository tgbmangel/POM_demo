# coding:utf8


import os
from time import sleep
from pages.sch_info_mana_page_add_scho import SchoolInfoManageAddPag
from common.resource_action import ResourceHelper
from common.my_unittest import MyUnitTestCase

class SchoolAdd(MyUnitTestCase):
    '''学校管理-添加学校'''
    def setUp(self):
        self.login_manage()
        self.url="http://{}/eduManager#/login".format(self.host_manage_page)
        # self.add_url="http://10.16.3.26:8068/eduManager#/end/scho-info-mana/add-scho"
        self.add_url='http://{}/eduManager#/end/add-scho'.format(self.host_manage_page)
        self.scho_add=SchoolInfoManageAddPag(self.driver,self.add_url, u"新增学校页面")
        self.resource_helper=ResourceHelper()
        self.test_data1=self.resource_helper.read_excel("scho_add_test_data.xls","Sheet1")

    #解析EXCEL数据并写入界面，然后判断保存按钮的流程封装
    def write_in_data(self,shco_add,test_data1):
        shco_add.open()
        shco_add.input_scho_name(test_data1[0])
        shco_add.input_scho_chin_name(test_data1[1])
        shco_add.input_scho_eng_name(test_data1[2])
        shco_add.input_scho_eng_s_name(test_data1[3])
        shco_add.input_scho_code(test_data1[4])
        shco_add.school_class_drop_select(int(test_data1[5]))
        shco_add.school_dis_drop_select(int(test_data1[6]))
        shco_add.school_location_select(int(test_data1[8]))
        shco_add.school_temp_drop_select(int(test_data1[7]))
        sleep(2)
        shco_add.input_detail_location(test_data1[9])
        shco_add.input_scho_master(test_data1[10])
        test_data_date_string=self.resource_helper.get_excel_date(test_data1[11])
        shco_add.input_scho_create_time(test_data_date_string)
        shco_add.upload_image(test_data1[12])
        sleep(2)
        self.assertEqual(shco_add.save_button_enable(),bool(int(test_data1[13])))

    #测试用例↓
    def test_case_add_success(self):
        '''全字段添加添加验证'''
        self.write_in_data(self.scho_add,self.test_data1[0])
    def test_ness_en_suoxie(self):
        '''必填项：缩写验证'''
        self.write_in_data(self.scho_add, self.test_data1[1])
    def test_ness_scho_code(self):
        '''必填项：学校代码验证'''
        self.write_in_data(self.scho_add, self.test_data1[2])
    def test_ness_detail_location(self):
        '''必填项：详细地址验证'''
        self.write_in_data(self.scho_add, self.test_data1[3])


#unittest 加入TestSuite后，对用例进行管理执行，以下代码用作单文件调试，可不写。↓
if __name__ == "__main__":
    from common.debug_run_action import DebugRunTest
    report_file_name = os.path.basename(__file__)[:-3]
    a=DebugRunTest(report_file_name)
    a.suiteTest.addTest(SchoolAdd("test_case_add_success"))
    a.suiteTest.addTest(SchoolAdd("test_ness_en_suoxie"))
    a.suiteTest.addTest(SchoolAdd("test_ness_scho_code"))
    a.suiteTest.addTest(SchoolAdd("test_ness_detail_location"))
    a.run()