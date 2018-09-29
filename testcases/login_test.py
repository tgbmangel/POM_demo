# coding=utf-8


from time import sleep
from pages.login_page import LoginPage
from common.my_unittest import MyUnitTestCase
class Caselogin(MyUnitTestCase):
    ''' 教育网页-登录页测试用例 '''
    url = "http://10.16.3.26:8067/edu/auth/login"
    username = u"wivElTrYdO"
    password = "12345678"
    def test_login(self):
        '''登录测试'''
        loginpage=LoginPage(self.driver, self.url, "10.16.3.26:8067/edu/auth/login")
        loginpage.open()
        sleep(3)
        loginpage.input_username(self.username)
        loginpage.input_password(self.password)
        #loginpage.click_submit()
        sleep(3)
        loginpage.click_submit()
        self.assertEqual(loginpage.show_userid(), u'溆浦一中')


#unittest 加入TestSuite后，对用例进行管理执行，以下代码用作单文件调试，可不写。↓

if __name__ == "__main__":
    from common.debug_run_action import DebugRunTest
    import os
    report_file_name = os.path.basename(__file__)[:-3]
    a=DebugRunTest(report_file_name)
    a.suiteTest.addTest(Caselogin("test_login"))
    a.run()