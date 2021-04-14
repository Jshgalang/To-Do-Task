import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.common.exceptions import WebDriverException
from unittest import skip


MAX_WAIT = 10 # catch random glitches / random slowdowns




class FunctionalTest(StaticLiveServerTestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    # def check_for_row_in_list_table(self, row_text):
    #     table = self.browser.find_element_by_id('id_list_table')
    #     rows = table.find_elements_by_tag_name('tr')
    #     self.assertIn(row_text, [row.text for row in rows])


    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True: # we're adding a polling logic to prev. check for row...
            try:
                table = self.browser.find_element_by_id('id_list_table')
                # table = self.browser.find_element_by_id('id_nothing')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                # self.assertIn('foo', [row.text for row in rows])
                return rows
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)
 
    def wait_for(self, func):
        start_time = time.time()
        while True: # we're adding a polling logic to prev. check for row...
            try:
                # table = self.browser.find_element_by_id('id_list_table')
                # # table = self.browser.find_element_by_id('id_nothing')
                # rows = table.find_elements_by_tag_name('tr')
                # self.assertIn(row_text, [row.text for row in rows])
                # # self.assertIn('foo', [row.text for row in rows])
                return func()
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def get_item_inputbox(self):
        return self.browser.find_element_by_id('id_text')

# setUp
# tearDown
# wait_for_row_in_list_table


