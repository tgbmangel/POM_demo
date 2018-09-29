# coding=utf-8

import os
from pages.resources_page import ResourcePage
from common.my_unittest import MyUnitTestCase

class ResouceSearch(MyUnitTestCase):
    '''教育网页-资源中心页面测试'''
    def setUp(self):
        self.login_manage()
        self.url = "http://10.16.3.26:8067/edu/resources"
        self.center_url='http://10.16.3.26:8067/edu/user-center/home'
        self.search_key_word="sss"
    def test_page_title(self):
        '''网页标题验证'''
        resource_page = ResourcePage(self.driver, self.url, u"资源列表")
        resource_page.open()
        resource_page.on_page(u"资源列表")

    def test_search_string(self):
        '''搜索字段验证'''
        resource_page = ResourcePage(self.driver, self.url, u"资源列表")
        resource_page.open()
        resource_page.input_search_comment(self.search_key_word)
        resource_page.click_submit()
        resource_page.click_link_text_xiti()


#unittest 加入TestSuite后，对用例进行管理执行，以下代码用作单文件调试，可不写。↓
if __name__ == "__main__":
    from common.debug_run_action import DebugRunTest
    report_file_name = os.path.basename(__file__)[:-3]
    a=DebugRunTest(report_file_name)
    a.suiteTest.addTest(ResouceSearch("test_page_title"))
    a.suiteTest.addTest(ResouceSearch("test_search_string"))
    a.suiteTest.addTest(ResouceSearch("test_personal_center"))
    a.run()