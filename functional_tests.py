import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class MikeTest(unittest.TestCase):
	@classmethod
	def setUp(self):
		self.browser = webdriver.Firefox()

	@classmethod
	def tearDown(self):
		self.browser.quit()

	# helper method
	def check_for_row_in_list_table(self, row_text):
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])

	def test_start_a_list_and_retrieve_it_later(self):
		self.browser.get("http://localhost:8000")
		self.assertIn('To-Do', self.browser.title)
		# header_text = self.browser.find_element_by_tag_name('h1').text
		# self.assertIn('To-Do', header_text)
		# self.browser.find_element_by_id('id_new_item')

		# Insert entry user story
		inputbox = self.browser.find_element_by_id('id_new_item')
		# self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a To-Do item.')
		inputbox.send_keys('Mike will eat a meatball')
		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)

		# update page reflecting text type 
		self.check_for_row_in_list_table('1: Mike will ear a meatball')
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		# self.assertTrue(any(row.text == '1: Mike will eat a meatball.' for row in rows), f"New to-do item did not appear in table. Contents were: \n{table.text}")
		self.assertIn('1: Mike will eat a meatball', [row.text for row in rows])
		self.assertIn('2: Mike will digest the meatball', [row.text for row in rows])

		# site should generate an url storing the TO-DO list
		self.fail('Finish the test!')

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

if __name__ == '__main__':
	unittest.main(warnings='ignore')
