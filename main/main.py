# coding:cp936
'''
ִ��������������
'''
from common import HTMLTestRunner
import unittest
import os
import sys


if __name__=="__main__":
    #�����ļ�Ŀ¼
    testcase_dir="../testcases/mini_manage_testcases/"
    #�����ļ���׺
    partern_file='*_test.py'
    suiteTest=unittest.defaultTestLoader.discover(testcase_dir,pattern=partern_file)
    report_file_name = os.path.basename(__file__)[:-3]
    filePath = "../report/{}.html".format(report_file_name)
    fp = open(filePath, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='{} TestReport'.format(report_file_name),
        description='This is {} Report'.format(report_file_name)
    )
    runner.run(suiteTest)