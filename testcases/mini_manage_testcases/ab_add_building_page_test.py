# -*- coding: utf-8 -*-
# @Project : POM_demo 
# @Time    : 2018/5/30 13:47
# @Author  : 
# @File    : ab_add_building_page_test.py
# @Software: PyCharm Community Edition
from pages.add_building_page import SchoolAddBuilding
from common.my_unittest import MyUnitTestCase
import time

class BuildAdd(MyUnitTestCase):
    '''学校内添加建筑'''
    def setUp(self):
        self.page_url='http://{}/eduManager#/end/build-info-mana-sm'.format(self.host_manage_page)
        config=self.readconfig()
        school_name=config.get("School","school_name")
        self.user_name=self.get_user_account(school_name)
        # user_name='xtgly001'
        self.pwd='12345678'
        now_time = time.strftime('%Y%m%d%H%M%S', time.localtime())
        self.build_number='bdn{}'.format(now_time)
        self.build_name=u"建筑{}".format(now_time)
        self.build_floors=100
        self.build_type=0
        #
        self.classroom_number='cr{}'.format(now_time)
        self.classroom_name='教室{}'.format(now_time)
        self.classroom_floor=1

        self.add_build=SchoolAddBuilding(self.driver, self.page_url, 'title')

    def test_add_build(self):
        '''添加建筑'''
        self.login_manage(self.user_name, self.pwd)
        self.add_build.open()
        time.sleep(2)
        self.add_build.click_add_button()
        self.add_build.input_build_no(self.build_number)
        self.add_build.input_build_name(self.build_name)
        self.add_build.input_build_floors(self.build_floors)
        self.add_build.input_build_use_type(self.build_type)
        time.sleep(1)
        self.add_build.save_build_add()
        time.sleep(5)
    def test_add_classroom(self):
        '''添加教室'''
        self.login_manage(self.user_name, self.pwd)
        self.add_build.open()
        time.sleep(2)
        self.add_build.click_manage_classroom_button()
        self.add_build.click_add_classroom_button()
        self.add_build.input_classroom_no(self.classroom_number)
        self.add_build.input_classroom_name(self.classroom_name)
        self.add_build.select_classroom_type(1)
        self.add_build.input_classroom_floor(self.classroom_floor)
        time.sleep(1)
        self.add_build.save_classroom_add()
#unittest 加入TestSuite后，对用例进行管理执行，以下代码用作单文件调试，可不写。↓
if __name__ == "__main__":
    from common.debug_run_action import DebugRunTest
    import os
    report_file_name = os.path.basename(__file__)[:-3]
    a=DebugRunTest(report_file_name)
    # a.suiteTest.addTest(BuildAdd("test_add_build"))
    for x in range(1,10):
        a.suiteTest.addTest(BuildAdd("test_add_classroom"))
    a.run()
