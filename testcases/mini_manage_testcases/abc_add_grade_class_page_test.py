# -*- coding: utf-8 -*-
# @Project : POM_demo 
# @Time    : 2018/5/30 16:19
# @Author  : 
# @File    : abc_add_grade_class_page_test.py
# @Software: PyCharm Community Edition

from pages.add_grade_class_page import SchoolAddGradeClass
from common.my_unittest import MyUnitTestCase
import time

class GradeClassAdd(MyUnitTestCase):
    '''学校内添加班级'''
    def setUp(self):
        self.page_url='http://{}/eduManager#/end/cla-area-mana-sm'.format(self.host_manage_page)
        config=self.readconfig()
        school_name=config.get("School","school_name")
        self.user_name=self.get_user_account(school_name)
        self.pwd='12345678'
        now_time = time.strftime('%Y%m%d%H%M%S', time.localtime())
        #
        self.class_no='bj{}'.format(now_time)
        self.class_name=u"班级{}".format(now_time)
        self.class_year=2018
        self.class_grade_index=0
        self.class_room_build_index=0
        self.class_room_room_index=0
        #
        self.add_class=SchoolAddGradeClass(self.driver, self.page_url, 'title')
    def test_add_class_grade(self):
        '''班级添加'''
        self.login_manage(self.user_name, self.pwd)
        self.add_class.open()
        time.sleep(2)
        self.add_class.click_add_class_grade()
        time.sleep(1)
        self.add_class.input_class_no_id(self.class_no)
        self.add_class.input_class_name(self.class_name)
        self.add_class.input_class_year(self.class_year)
        self.add_class.select_class_grade(self.class_grade_index)
        self.add_class.select_class_room(self.class_room_build_index,self.class_room_room_index)
        self.add_class.save_class_add()

#unittest 加入TestSuite后，对用例进行管理执行，以下代码用作单文件调试，可不写。↓
if __name__ == "__main__":
    from common.debug_run_action import DebugRunTest
    import os
    report_file_name = os.path.basename(__file__)[:-3]
    a=DebugRunTest(report_file_name)
    a.suiteTest.addTest(GradeClassAdd("test_add_class_grade"))
    a.run()
