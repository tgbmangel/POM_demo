#coding:utf8
'''
配置浏览器驱动
'''
from selenium import webdriver
import os
import sys

class StartBrowser(object):
    def __init__(self,driver_name="chrome"):
        '''
        初始化时默认使用chrome浏览器
        :param driver_name:浏览器类型名称：chrome，firefox，ie
        '''
        self.driver_name=driver_name
        self.dir_path=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath("."))),"tools")
        print('driver path：{}'.format(self.dir_path))
        self.chrome_driver_path=os.path.join(self.dir_path,"chromedriver.exe")
        self.firefox_driver_path=os.path.join(self.dir_path,"geckodriver.exe")
        self.ie_driver_path = os.path.join(self.dir_path , "Iedriver.exe")
        sys.path.append(self.dir_path)
        self.start_browser()
    def start_browser(self):
        if self.driver_name=="chrome":
            try:
                self.driver = webdriver.Chrome(self.chrome_driver_path)
            except Exception as e:
                print(e)
        elif self.driver_name=='firefox':
            try:
                self.driver=webdriver.Firefox()
            except Exception as e:
                print(e)
        elif self.driver_name=='ie':
            try:
                self.driver=webdriver.Ie(self.ie_driver_path)
            except Exception as e:
                print(e)
        else:
            try:
                self.driver = webdriver.Chrome()
            except Exception as e:
                print(e)
        self.driver.implicitly_wait(30)

