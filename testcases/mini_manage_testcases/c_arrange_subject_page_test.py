# -*- coding: utf-8 -*-
# @Project : POM_demo 
# @Time    : 2018/5/31 11:44
# @Author  : 
# @File    : c_arrange_subject_page_test.py
# @Software: PyCharm Community Edition
from pages.arrange_subject_page import ArrangeSubject
from pages.arrange_group_page import ArrangeGroup
from pages.arrange_lesson_page import ArrangeLesson
from common.my_unittest import MyUnitTestCase
import time
class SubjectArrange(MyUnitTestCase):
    '''学校内教务教学管理安排'''
    def setUp(self):
        self.page_url = 'http://{}/eduManager#/end/teach-arrange-sub'.format(self.host_manage_page)
        self.group_url='http://{}/eduManager#/end/teach-arrange-group'.format(self.host_manage_page)
        self.lesson_url='http://{}/eduManager#/end/teach-arrange-lesson'.format(self.host_manage_page)
        config=self.readconfig()
        school_name=config.get("School","school_name")
        self.user_name=self.get_user_account(school_name)
        self.subject_arrange=ArrangeSubject(self.driver,self.page_url,'title')
        self.group_arrange=ArrangeGroup(self.driver,self.group_url,'title')
        self.lesson_arrange=ArrangeLesson(self.driver,self.lesson_url,'title')
    def test_a_arrange_subject(self):
        '''学科安排'''
        self.login_manage(self.user_name,self.pwd)
        self.subject_arrange.open()
        self.subject_arrange.click_arrange_button()
        self.subject_arrange.select_all_box()
        self.subject_arrange.add_arrange()
        self.subject_arrange.save_arrange()
        time.sleep(5)
    def test_b_arrange_group(self):
        '''教研组安排'''
        self.group_arrange.open()
        self.group_arrange.select_drop_selection()
        self.group_arrange.save_arrange_group()
        time.sleep(5)
    def test_c_arrange_group(self):
        '''备课组安排'''
        self.lesson_arrange.open()
        self.lesson_arrange.select_drop_selection()
        self.lesson_arrange.save_arrange_lesson()
        time.sleep(5)


#unittest 加入TestSuite后，对用例进行管理执行，以下代码用作单文件调试，可不写。↓
if __name__ == "__main__":
    from common.debug_run_action import DebugRunTest
    import os
    report_file_name = os.path.basename(__file__)[:-3]
    a=DebugRunTest(report_file_name)
    a.suiteTest.addTest(SubjectArrange("test_a_arrange_subject"))
    a.suiteTest.addTest(SubjectArrange("test_c_arrange_group"))
    a.run()