# coding=utf-8

from selenium.webdriver.common.by import By
from pages.basepage import BasePage

class ResourcePage(BasePage):
    '''资源中心'''
    search_input_xpath='//*[@id="resource-search"]/nz-input/input'
    search_button='//*[@id="resource-search"]/nz-input/span'
    xiti_text='//*[@id="condition-type"]/edu-tab-nav2/div/div/div/a[13]'
    search_comment_loc=(By.XPATH, search_input_xpath)
    submit_loc=(By.XPATH,search_button)
    xiti_text_area=(By.XPATH,xiti_text)

    def open(self):
        self._open(self.base_url, self.pagetitle)
    def input_search_comment(self, search_comment):
        self.find_element(*self.search_comment_loc).send_keys(search_comment)
    def click_submit(self):
        self.find_element(*self.submit_loc).click()
    def click_link_text_xiti(self):
        self.find_element(*self.xiti_text_area).click()