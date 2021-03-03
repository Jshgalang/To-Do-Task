import unittest
from selenium import webdriver

class MikeTest(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_add_entry_and_retrieve_later(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('To Do', self.browser.title,f'Browser title was {self.browser.title}')
        self.fail('Finish the Test')

        # enable the user to insert an entry
        # user types into the textbox
        # page updates and reflects content of textbox after entering
        # continuous entry
        # site should generate a url storing the TO-DO list
        # user visits the URL to show the generated TO-DO list


if __name__ == '__main__':
    unittest.main(warnings='ignore')


"""
# browser open
browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'TO-DO' in browser.title, f'Browser title was {browser.title}' # first thing the user will see

# enable the user to insert an entry
# user types into the textbox
# page updates and reflects content of textbox after entering
# continuous entry
# site should generate a url storing the TO-DO list
# user visits the URL to show the generated TO-DO list


browser.quit()
"""

