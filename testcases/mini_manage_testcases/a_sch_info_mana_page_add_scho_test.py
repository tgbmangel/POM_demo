# -*- coding: utf-8 -*-
# @Project : POM_demo 
# @Time    : 2018/5/29 15:03
# @Author  : 
# @File    : a_sch_info_mana_page_add_scho_test.py
# @Software: PyCharm Community Edition

import os
import time
from pages.sch_info_mana_page_add_scho import SchoolInfoManageAddPag
from common.my_unittest import MyUnitTestCase

class SchoolAdd(MyUnitTestCase):
    '''学校管理-添加学校'''
    def setUp(self):
        self.login_manage()
        self.url="http://{}/eduManager#/login".format(self.host_manage_page)
        # self.add_url="http://10.16.3.26:8068/eduManager#/end/scho-info-mana/add-scho"
        self.add_url='http://{}/eduManager#/end/add-scho'.format(self.host_manage_page)
        self.scho_add=SchoolInfoManageAddPag(self.driver,self.add_url, u"新增学校页面")
        if os.path.exists(self.ini_file):
            os.remove(self.ini_file)
    #测试用例↓
    def test_case_add_success(self):
        '''添加成功验证'''
        config = self.readconfig()
        config.add_section("School")
        self.scho_add.open()
        now_time=time.strftime('%Y%m%d%H%M%S',time.localtime())
        config.set("School", "school_name", now_time)
        self.save_config(config)
        scho_name = u'学校{}'.format(now_time)
        self.scho_add.input_scho_name(scho_name)
        self.scho_add.input_scho_code('py{}'.format(now_time))
        self.scho_add.school_dis_drop_select(1)
        self.scho_add.school_temp_drop_select(1)
        self.scho_add.school_type_drop_select(0)
        time.sleep(2)
        self.scho_add.input_scho_master(u'王校长')
        time.sleep(5)#
        self.scho_add.save_info_click()
        time.sleep(15)
        # a=self.scho_add.success_info()
        # self.assertEqual(a,True)



#unittest 加入TestSuite后，对用例进行管理执行，以下代码用作单文件调试，可不写。↓
if __name__ == "__main__":
    from common.debug_run_action import DebugRunTest
    report_file_name = os.path.basename(__file__)[:-3]
    a=DebugRunTest(report_file_name)
    a.suiteTest.addTest(SchoolAdd("test_case_add_success"))
    a.run()