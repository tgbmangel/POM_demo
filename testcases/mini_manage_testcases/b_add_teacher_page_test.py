#coding:utf8
from pages.add_teacher_page import TeacherInfoAddTeacher
from common.my_unittest import MyUnitTestCase

import time
class TeacherAdd(MyUnitTestCase):
    '''学校内添加老师'''
    def setUp(self):
        self.page_url='http://{}/eduManager#/end/teach-info-mana-sm'.format(self.host_manage_page)
        config=self.readconfig()
        school_name=config.get("School","school_name")
        self.user_name=self.get_user_account(school_name)
        # user_name='xtgly001'
        self.pwd='12345678'
        now_time = time.strftime('%Y%m%d%H%M%S', time.localtime())
        self.teacher_name=u'老师{}'.format(now_time)
        self.teacher_account='fcsxls'
        self.teacher_sex=1
        self.teacher_nation=u'维吾尔族'
        self.teacher_no_id= '4307261989{}{}'.format(now_time[4:8],now_time[-4:])
        self.teacher_huji=u'湖南'
        self.teacher_address=u'湖南北京'
        self.teacher_address_now=u'湖南北京区'
        self.teacher_birthday='2000-10-22'
        self.teacher_phone='135{}{}'.format(now_time[4:8],now_time[-4:])
        self.add_teacher=TeacherInfoAddTeacher(self.driver,self.page_url,'title')

    def test_add_sucess(self):
        '''添加成功验证'''
        self.login_manage(self.user_name, self.pwd)
        self.add_teacher.open()
        self.add_teacher.add_teacher_in_scholl_button_click()
        self.add_teacher.input_teacher_name(self.teacher_name)
        self.add_teacher.input_teacher_id(self.teacher_no_id)
        self.add_teacher.input_teacher_phone(self.teacher_phone)
        self.add_teacher.select_teacher_nation(1)
        self.add_teacher.select_teacher_zhizhengmianmao(1)
        self.add_teacher.select_teacher_zhicheng(1)
        self.add_teacher.save_teacher_info()
        time.sleep(5)
    def test_arrange_partment(self):
        '''教师安排'''
        self.add_teacher.click_partment_arrange()
        time.sleep(3)
        self.add_teacher.check_all_box()
        self.add_teacher.save_partment_arrange()


#unittest 加入TestSuite后，对用例进行管理执行，以下代码用作单文件调试，可不写。↓
if __name__ == "__main__":
    from common.debug_run_action import DebugRunTest
    import os
    report_file_name = os.path.basename(__file__)[:-3]
    a=DebugRunTest(report_file_name)
    a.suiteTest.addTest(TeacherAdd("test_add_sucess"))
    a.suiteTest.addTest(TeacherAdd("test_arrange_partment"))
    a.run()

