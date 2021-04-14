# import unittest
# import time
# from django.test import LiveServerTestCase
# from django.contrib.staticfiles.testing import StaticLiveServerTestCase
# from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.common.exceptions import WebDriverException
# from unittest import skip

from .base import FunctionalTest

# MAX_WAIT = 10 # catch random glitches/ random slowdowns

class LayoutAndStylingTest(FunctionalTest):
	def test_layout_and_styling(self):
		# Mike goes to homepage
		self.browser.get(self.live_server_url)
		self.browser.set_window_size(1024, 768)
		# Mike sees input box at the center
		# inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox = self.get_item_input_box()
		self.assertAlmostEqual(
			inputbox.location['x'] + inputbox.size['width'] / 2,
		 	512, 
		 	delta = 10,
		 	)

		# mike starts a new list and sees it's also centered
		inputbox.send_keys('testing')		
		inputbox.send_keys(Keys.ENTER)
		self.wait_for_row_in_list_table('1: testing')
		# inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox = self.get_item_input_box()
		self.assertAlmostEqual(
			inputbox.location['x'] + inputbox.size['width'] / 2,
		 	512, 
		 	delta = 10,
		 	)
