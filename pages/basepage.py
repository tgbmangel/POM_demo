# coding=utf-8
'''
Project:基础类BasePage，封装所有页面都公用的方法，
定义open函数，重定义find_element，switch_frame，send_keys等函数。
在初始化方法中定义驱动driver，基本url，title
WebDriverWait提供了显式等待方式。
'''
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from ctypes import *
import win32api,win32gui
import win32con
import time

class BasePage(object):
    """
    BasePage封装所有页面都公用的方法，例如driver, url ,FindElement等
    """
    # 初始化driver、url、pagetitle等
    # 实例化BasePage类时，最先执行的就是__init__方法，该方法的入参，其实就是BasePage类的入参。
    # __init__方法不能有返回值，只能返回None
    # self只实例本身，相较于类Page而言。
    def __init__(self, selenium_driver, base_url, pagetitle):
        self.driver = selenium_driver
        self.base_url = base_url
        self.pagetitle = pagetitle

    # 通过title断言进入的页面是否正确。
    # 使用title获取当前窗口title，检查输入的title是否在当前title中，返回比较结果（True 或 False）
    def on_page(self, pagetitle):
        return pagetitle in self.driver.title

    # 打开页面，并校验页面链接是否加载正确
    # 以单下划线_开头的方法，在使用import *时，该方法不会被导入，保证该方法为类私有的。
    def _open(self, url, pagetitle):
        # 使用get打开访问链接地址
        self.driver.get(url)
        self.driver.maximize_window()
        # 使用assert进行校验，打开的窗口title是否与配置的title一致。调用on_page()方法
        #assert self.on_page(pagetitle), u"打开开页面失败 %s" % url

    # 定义open方法，调用_open()进行打开链接
    def open(self):
        self._open(self.base_url, self.pagetitle)
        self.wait_time_second(5)
    #refresh
    def fresh_page(self):
        self.driver.refresh()
    # 重写元素定位方法
    def find_element(self, *loc):
        #        return self.driver.find_element(*loc)
        try:
            # 确保元素是可见的。
            # 注意：以下入参为元组的元素，需要加*。Python存在这种特性，就是将入参放在元组里。
            #            WebDriverWait(self.driver,10).until(lambda driver: driver.find_element(*loc).is_displayed())
            # 注意：以下入参本身是元组，不需要加*
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            print(u"%s 页面中未能找到 %s 元素" % (self, loc))
    #
    def find_elements(self, *loc):
        #        return self.driver.find_elements(*loc)
        try:
            # 确保元素是可见的。
            # 注意：以下入参为元组的元素，需要加*。Python存在这种特性，就是将入参放在元组里。
            #            WebDriverWait(self.driver,10).until(lambda driver: driver.find_element(*loc).is_displayed())
            # 注意：以下入参本身是元组，不需要加*
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_elements(*loc)
        except:
            print(u"%s 页面中未能找到 %s 元素" % (self, loc))

    def get_element_by_xpath(self,xpath):
        '''
        封装常用方法：xpath
        :param xpath: 网页元素的xpath，通过F12查看，右键copy Xpath即可
        :return: 返回element对象
        '''
        try:
            return self.driver.find_element_by_xpath(xpath)
        except:
            print(u"%s 页面中未能找到 %s 元素" % (self,xpath))
    def get_select_element_by_xpath(self,div_xpath,drop_list_li_xpath,index):
        '''
        下拉控件封装
        :param xpath:
        :param index:
        :return:
        '''
        self.driver.find_element_by_xpath(div_xpath).click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of(self.driver.find_element_by_xpath(drop_list_li_xpath)))
        lis = self.driver.find_elements_by_xpath(drop_list_li_xpath)
        lis[index].click()

    def get_date_element_by_xpath(self,xpath,classname,index):
        '''
        日期控件
        :param xpath:日期控件的xpath
        :param classname: 如：日期控件input class="ant-calendar-picker-input ant-input" ，则classname="ant-calendar-picker-input ant-input"
        :param index:该日期控件属于同class 的第几个,第一个就填1，在查询时会进行减一，从零开始
        :return:
        '''
        js = "var list=document.getElementsByClassName(\"{}\");list[{}].removeAttribute('readonly');".format(classname,index-1)
        try:
            self.driver.execute_script(js)
            return self.driver.find_element_by_xpath(xpath)
        except Exception as e:
            print(e)
    def get_elements_by_xpath(self, box_xpath):
        '''
        获取checkbox(或者其他控件）
        :param box_xpath:
        :return: list of check boxes in current page 当前页面所有的box
        '''
        return self.driver.find_elements_by_xpath(box_xpath)
    def get_element_by_link_text(self,linktext):
        '''
        :param linktext:
        :return:
        '''
        return  self.driver.find_element_by_partial_link_text(linktext)
    def brower_actions_enter(self):
        '''
        浏览器ENTER按钮
        :return: __actions
        '''
        __actions=ActionChains(self.driver)
        __actions.key_down(Keys.ENTER)
        __actions.perform()
    def brower_actions_esc(self):
        '''
        浏览器上按下ESCAPE，主要用户部分控件无法自动返回，则使用该方法返回原状。
        :return: __actions
        '''
        __actions=ActionChains(self.driver)
        __actions.key_down(Keys.ESCAPE)
        __actions.perform()

    def browser_action_scroll_dwon(self):
        '''
        滚动到页面底部
        :return:
        '''
        js = "var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)
    def browser_scroll_to_element(self,element):
        '''
        滚动到element可见的位置
        :param element: element对象
        :return:
        '''
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def clear_element_by_xpath(self,xpath):
        WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_xpath(xpath)).clear()
    def click_element_by_xpath(self,xpath):
        WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_xpath(xpath)).click()

    # 重写switch_frame方法
    def switch_frame(self, loc):
        return self.driver.switch_to_frame(loc)

    # 定义script方法，用于执行js脚本，范围执行结果
    def script(self, src):
        self.driver.execute_script(src)

    # 重写定义send_keys方法
    def send_keys(self, loc, vaule, clear_first=True, click_first=True):
        try:
            loc = getattr(self, "_%s" % loc)  # getattr相当于实现self.loc
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(vaule)
        except AttributeError:
            print(u"%s 页面中未能找到 %s 元素" % (self, loc))
    #wait
    def wait_time_second(self,seconds):
        '''
        页面等待。区别于sleep
        :param seconds:
        :return:
        '''
        self.driver.implicitly_wait(seconds)
    def mouse_move_to(self,x,y):
        '''
        :param x: 光标移动到的x坐标
        :param y: 光标移动到的y坐标
        '''
        windll.user32.SetCursorPos(x,y)
    def mouse_move_and_click(self,x,y):
        #移动到坐标位置并点击
        windll.user32.SetCursorPos(x,y)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y)
        time.sleep(0.05)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y)
        time.sleep(0.5)