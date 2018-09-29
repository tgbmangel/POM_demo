# coding=utf-8

from selenium.webdriver.common.by import By
from pages.basepage import BasePage

class PersonalCenterPage(BasePage):
    '''个人中心'''
    blog_input_xpath='//*[@id="inputArea"]'
    release_button_xpath='//*[@id="publish-dynamic"]/edu-publish-dynamic/div/div/div/div[1]/div[2]/button'
    blog_input_loc=(By.XPATH,blog_input_xpath)
    release_button_loc=(By.XPATH,release_button_xpath)

    def open(self):
        self._open(self.base_url, self.pagetitle)
    def blog_input(self,blog_comment):
        self.find_element(*self.blog_input_loc).sendkey(blog_comment)
    def release_blog(self):
        self.find_element(*self.release_button_loc).click()