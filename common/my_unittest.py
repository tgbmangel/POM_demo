#coding:utf8
'''
将unittest封装，子类继承时不需要再去加载浏览器驱动
子类继承时，直接self.driver 进行使用驱动，且可以通过调用setup做用例初始化。
'''
import unittest
from common.browser_action import StartBrowser
from pages.login_page import LoginPage
import configparser
from time import sleep
import os
from common.database_action import PostgreSQL_Connect
import time

class MyUnitTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = StartBrowser().driver
        cls.host_manage_page= "222.244.147.121:8068"
        cls.database_ip="10.16.4.57"
        cls.database_db="wisdom_education_service_pre"
        cls.database_user="postgres"
        cls.database_pwd="aorise"
        cls.ini_file="Config.ini"
        cls.image_path=r'{}\resource_file\bd_logo1.png'.format(os.path.dirname(os.path.abspath(".")))
        cls.pwd='12345678'
        cls.now_time = time.strftime('%Y%m%d%H%M%S', time.localtime())

    @classmethod
    def tearDownClass(cls):
        sleep(5)
        cls.driver.quit()
        pass

    def browser_driver(self):
        return self.driver

    def login_manage(self,user_name=u'xtgly001',pwd='12345678'):
        url = "http://{}/eduManager#/login".format(self.host_manage_page)
        loginpage = LoginPage(self.driver, url, "教育大主页")
        loginpage.open()
        sleep(3)
        # 目前登录框会自动加载一个用户名和密码，正常需要输入特定账号进行测试
        loginpage.input_manage_page_name(user_name)
        loginpage.input_manage_page_pwd(pwd)
        loginpage.login_manage_page()
        sleep(2)
        loginpage.fresh_page()

    def login_operation_manage(self,user_name=u'yygly001',pwd='12345678'):
        url = "http://{}/eduManager#/login".format(self.host_manage_page)
        loginpage = LoginPage(self.driver, url, "教育大主页")
        loginpage.open()
        sleep(3)
        # 目前登录框会自动加载一个用户名和密码，正常需要输入特定账号进行测试
        loginpage.input_manage_page_name(user_name)
        loginpage.input_manage_page_pwd(pwd)
        loginpage.login_manage_page()
        sleep(2)
        loginpage.fresh_page()

    def login(self):
        url = "http://{}/edu/auth/login".format(self.host_manage_page)
        loginpage = LoginPage(self.driver, url, "title")
        loginpage.open()
        sleep(3)
        # 目前登录框会自动加载一个用户名和密码，正常需要输入特定账号进行测试
        loginpage.click_submit()
        sleep(3)
        loginpage.fresh_page()

    def readconfig(self):
        config = configparser.ConfigParser()
        config.read(self.ini_file)
        return config
    def save_config(self,config):
        fp=open(self.ini_file, "w")
        config.write(fp)
        fp.close()
    def get_user_account(self,school_name):
        S=PostgreSQL_Connect(self.database_db,self.database_user,self.database_pwd,self.database_ip)
        sql="select user_account from sys_user_detail where user_name like '%%{}%%'".format(school_name)
        user_name=S.executesql(sql)[0]
        S.close_connection()
        return user_name