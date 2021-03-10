import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class MikeTest(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()


    def tearDown(self) -> None:
        self.browser.quit()


    # helper method
    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_test, [row.text for row in rows])


    def test_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('TO-DO', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text # user types into the textbox
        self.assertIn('Your To-Do List', header_text)
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a to-do item:') 
        inputbox.send_keys('Mike will eat a meatball') # enable the user to insert an entry
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)


        # page updates and reflects content of textbox after entering
        self.check_for_row_in_list_table('1: Mike will eat a meatball')
        self.check_for_row_in_list_table('2: Mike will digest the meatball')        

        # site should generate a url storing the TO-DO list
        self.fail('Finish the test!')


    def test_add_entry_and_retrieve_later(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('TO-DO', self.browser.title,f'Browser title was {self.browser.title}')
        self.fail('Finish the Test')

        
        
        
        # continuous entry
        #
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

