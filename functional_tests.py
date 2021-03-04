import unittest
from selenium import webdriver

class MikeTest(unittest.TestCase):
	@classmethod
	def setUp(self):
		self.browser = webdriver.Firefox()

	@classmethod
	def tearDown(self):
		self.browser.quit()

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
