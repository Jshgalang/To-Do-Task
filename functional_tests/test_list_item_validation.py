# import unittest
# from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# from django.test import LiveServerTestCase
# from django.contrib.staticfiles.testing import StaticLiveServerTestCase
# from selenium.common.exceptions import WebDriverException
from unittest import skip
from .base import FunctionalTest

MAX_WAIT = 10 # catch random glitches / random slowdowns

class ItemValidationTest(FunctionalTest):
    # cantaddemptylistitems
    # @skip
    def test_cannot_add_empty_list_items(self):
        # Mike goes to the home page and accidentally tries to submit
        # an empty list item. He hits ENTER on the empty input box


        # Home page refreshes, then error message pops up
        # saying list items cannot be blank

        # Mike tries again with some text for items, which now works

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

