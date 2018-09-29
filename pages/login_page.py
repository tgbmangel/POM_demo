# coding=utf-8

from selenium.webdriver.common.by import By
from pages.basepage import BasePage

# 继承BasePage类
class LoginPage(BasePage):
    '''登录页'''
    # 定位器，通过元素属性定位元素对象
    login_input_name_xpath = '//*[@id="content"]/div/div[2]/form/div[2]/div/div/nz-input/input'
    login_input_pwd_xpath = '//*[@id="content"]/div/div[2]/form/div[3]/div/div/nz-input/input'
    login_button_xpath = '//*[@id="content"]/div/div[2]/form/div[4]/div/div/button'
    login_manage_button_xpath='/html/body/education-root/div/login/nz-spin/div[2]/div/div/form/div[4]/div/div/button'
    error_text_xpath='//*[@id="content"]/div/div[2]/form/div[1]/div/div/span'
    userid_xpath='//*[@id="edu-info"]/span[1]'
    username_loc = (By.XPATH, login_input_name_xpath)
    password_loc = (By.XPATH, login_input_pwd_xpath)
    submit_loc = (By.XPATH, login_button_xpath)
    span_loc=(By.XPATH,error_text_xpath)
    userid_loc=(By.XPATH,userid_xpath)
    manage_page_login_loc=(By.XPATH,login_manage_button_xpath)
    manage_page_login_name_input_xpath='/html/body/education-root/div/login/nz-spin/div[2]/div/div/form/div[2]/div/div/nz-input/input'
    manage_page_login_pwd_input_xpath='/html/body/education-root/div/login/nz-spin/div[2]/div/div/form/div[3]/div/div/nz-input/input'
    # 打开网页
    def open(self):
        # 调用page中的_open打开连接
        self._open(self.base_url, self.pagetitle)

    # 输入用户名：调用send_keys对象，输入用户名
    def input_username(self, username):
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)

    # 输入密码：调用send_keys对象，输入密码
    def input_password(self, password):
        self.find_element(*self.password_loc).clear()
        self.find_element(*self.password_loc).send_keys(password)

    # 点击登录：调用send_keys对象，点击登录
    def click_submit(self):
        self.find_element(*self.submit_loc).click()

    # 用户名或密码不合理是Tip框内容展示
    def show_span(self):
        return self.find_element(*self.span_loc).text

    # 切换登录模式为动态密码登录（IE下有效）
    def swich_DynPw(self):
        self.find_element(*self.dynpw_loc).click()

    # 登录成功页面中的用户ID查找
    def show_userid(self):
        return self.find_element(*self.userid_loc).text

    #manage page login
    def login_manage_page(self):
        self.find_element(*self.manage_page_login_loc).click()

    def input_manage_page_name(self,user_name):
        self.get_element_by_xpath(self.manage_page_login_name_input_xpath).clear()
        self.get_element_by_xpath(self.manage_page_login_name_input_xpath).send_keys(user_name)

    def input_manage_page_pwd(self,pwd):
        self.get_element_by_xpath(self.manage_page_login_pwd_input_xpath).clear()
        self.get_element_by_xpath(self.manage_page_login_pwd_input_xpath).send_keys(pwd)