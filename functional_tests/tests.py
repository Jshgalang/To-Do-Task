import unittest
import time
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException

MAX_WAIT = 10 # catch random glitches/ random slowdowns

class MikeTest(LiveServerTestCase):
	@classmethod
	def setUp(self):
		self.browser = webdriver.Firefox()

	@classmethod
	def tearDown(self):
		self.browser.quit()

	# helper method
	# def check_for_row_in_list_table(self, row_text):
	# 	table = self.browser.find_element_by_id('id_list_table')
	# 	rows = table.find_elements_by_tag_name('tr')
	# 	self.assertIn(row_text, [row.text for row in rows])

	# renaming
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

	def test_start_a_list_and_retrieve_it_later(self):  # good for 1 user only
		# self.browser.get("http://localhost:8000")
		self.browser.get(self.live_server_url)

		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)
		self.browser.find_element_by_id('id_new_item')

		# Insert entry user story
		inputbox = self.browser.find_element_by_id('id_new_item')
		# self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a To-Do item.')
		inputbox.send_keys('Mike will eat a meatball')
		inputbox.send_keys(Keys.ENTER)
		# time.sleep(1)

		# update page reflecting text type 
		# self.check_for_row_in_list_table('1: Mike will eat a meatball')
		self.wait_for_row_in_list_table('1: Mike will eat a meatball')

		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Mike will digest the meatball')
		inputbox.send_keys(Keys.ENTER)
		# time.sleep(1)

		# self.check_for_row_in_list_table('1: Mike will eat a meatball')
		# self.check_for_row_in_list_table('2: Mike will digest the meatball')
		self.wait_for_row_in_list_table('1: Mike will eat a meatball')
		self.wait_for_row_in_list_table('2: Mike will digest the meatball')

		# table = self.browser.find_element_by_id('id_list_table')
		# rows = table.find_elements_by_tag_name('tr')
		# self.assertTrue(any(row.text == '1: Mike will eat a meatball.' for row in rows), f"New to-do item did not appear in table. Contents were: \n{table.text}")
		# self.assertIn('1: Mike will eat a meatball', [row.text for row in rows])
		# self.assertIn('2: Mike will digest the meatball', [row.text for row in rows])

		# site should generate an url storing the TO-DO list
		self.fail('Finish the test!')

	def test_multiple_users_can_start_lists_at_different_urls(self):  
		# Mike starts a new to-do list
		self.browser.get(self.live_server_url)
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Mike will eat a meatball')
		inputbox.send_keys(Keys.ENTER)

		# Mike sees his list has a unique URL
		mike_list_url = self.browser.current_url
		self.assertRegex(mike_list_url, '/lists/.+')
		# self.assertRegex(mike_list_url, '/lists/(\d+)')

		'''
		<assuming we have new users, we check that they dont see mike's list AND that they each have unique URLs>
		
		new user, Iso, comes along the site
		'''
		self.browser.quit()
		self.browser = webdriver.Firefox()
		
		# iso visits home page. no sign of mike's list
		self.browser.get(self.live_server_url)
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Mike will eat a meatball', page_text)
		self.assertNotIn('Mike will digest the meatball', page_text)

		# Iso starts a new list by adding a new item
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Buy milk')
		inputbox.send_keys(Keys.ENTER)
		self.wait_for_row_in_list_table('1: Buy milk')

		# Iso gets her own unique URL
		iso_list_url = self.browser.current_url
		self.assertRegex(iso_list_url, '/lists/.+')
		# self.assertRegex(iso_list_url, '/lists/(\d+)')
		self.assertNotEqual(iso_list_url, mike_list_url)

		# No trace of Mike's list dapat
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Mike will eat a meatball', page_text)
		self.assertIn('Buy milk', page_text)


	def test_addentry_and_retrievelater(self):  #  main func
		self.browser.get("http://localhost:8000")  # homepage checkout

		self.assertIn('To-Do', self.browser.title) # what the user sees upon loading the homepage
		self.fail('Finish the test.')

		# enable the user to insert an entry

		# user types item to the text box
		# update page reflecting text type
		# continuous entry
		# site should generate an url storing the TO-DO list

		# user should visit the url
		# browser.quit()

#  Accessing
# browser = webdriver.Firefox()
# browser.get("http://localhost:8000")

# assert 'TO-DO' in browser.title, 'Browser title was ' + browser.title #  First thing the user will see

# enable the user to insert an entry

# user types item to the text box
# update page reflecting text type
# continuous entry
# site should generate an url storing the TO-DO list

# user should visit the url
# browser.quit()

# if __name__ == '__main__':
# 	unittest.main(warnings='ignore')
