# import unittest
# from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# from django.test import LiveServerTestCase
# from django.contrib.staticfiles.testing import StaticLiveServerTestCase
# from selenium.common.exceptions import WebDriverException
from unittest import skip
from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):
    # cantaddemptylistitems
    # @skip
    def test_cannot_add_empty_list_items(self):
        # Mike goes to the home page and accidentally tries to submit
        # an empty list item. He hits ENTER on the empty input box
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)

        # Home page refreshes, then error message pops up
        # saying list items cannot be blank
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element_by_css_selector('.has-error').text, 
            "You can't have an empty list item."
        ))

        # Mike tries again with some text for items, which now works
        self.browser.find_element_by_id('id_new_item').send_keys('Buy milk')
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        # Then he decides to submit a second blank list item

        # He should receive a similar warning sa list page

        # Tapos icocorrect nya ulit by filling some text in
        self.fail('Write me!')
    


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

