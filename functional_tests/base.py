# import unittest
import time
# from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
# from unittest import skip

MAX_WAIT = 10 # catch random glitches/ random slowdowns


class FunctionalTest(StaticLiveServerTestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def wait_for_row_in_list_table(self, row_text):
		start_time = time.time()
		while True:  # we're adding a polling logic to prev. check_for_row...
			try:
				table = self.browser.find_element_by_id('id_list_table')
				# table = self.browser.find_element_by_id('id_nothing')
				rows = table.find_elements_by_tag_name('tr')
				self.assertIn(row_text, [row.text for row in rows])
				# self.assertIn('foo', [row.text for row in rows])
				return
			except (AssertionError, WebDriverException) as e:
			# AssertionError when the row asserted is still missing
			# WebdriverException if page is not loaded and selenium element is not loaded
				if time.time() - start_time > MAX_WAIT:
					raise e
				time.sleep(0.5)

	def wait_for(self, fn):
		# "every time you cause a reload, wait"
		start_time = time.time()
		while True:  # we're adding a polling logic to prev. check_for_row...
			try:
				# table = self.browser.find_element_by_id('id_list_table')
				# # table = self.browser.find_element_by_id('id_nothing')
				# rows = table.find_elements_by_tag_name('tr')
				# self.assertIn(row_text, [row.text for row in rows])
				# self.assertIn('foo', [row.text for row in rows])
				return fn()
			except (AssertionError, WebDriverException) as e:
			# AssertionError when the row asserted is still missing
			# WebdriverException if page is not loaded and selenium element is not loaded
				if time.time() - start_time > MAX_WAIT:
					raise e
				time.sleep(0.5)

	def get_item_input_box(self):
		return self.browser.find_element_by_id('id_text')