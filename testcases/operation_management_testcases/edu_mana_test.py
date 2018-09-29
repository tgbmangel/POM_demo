# -*- coding: utf-8 -*-
# @Project : POM_demo 
# @Time    : 2018/9/3 14:56
# @Author  : 
# @File    : edu_mana_test.py
# @Software: PyCharm

from pages.edu_mana_page import EduMana
from common.my_unittest import MyUnitTestCase
import time
class AddVolume(MyUnitTestCase):
    '''运营管理后台-册次信息管理-新增册次'''
    def setUp(self):
        time_now=time.strftime('%Y%m%d%H%M%S',time.localtime())
        self.volume_name_input='C{}'.format(time_now)
        self.vloume_short_input='CS{}'.format(time_now)
        page_url='http://{}/eduManager#/end/edu-mana'.format(self.host_manage_page)
        self.add_volume=EduMana(self.driver,page_url,'title')
    def test_add_volume(self):
        self.login_operation_manage()
        self.add_volume.open()
        self.add_volume.click_add_volume_button()
        time.sleep(0.5)
        self.add_volume.input_volume_name(self.volume_name_input)
        self.add_volume.input_volume_short_name(self.volume_name_input)
        self.add_volume.save_volume_info()


