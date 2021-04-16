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

class ItemValidationTest(FunctionalTest):
    # cantaddemptylistitems
    # @skip
    # def test_cannot_add_empty_list_items(self):
    #     # Mike goes to the home page and accidentally tries to submit
    #     # an empty list item. He hits ENTER on the empty input box
    #     self.browser.get(self.live_server_url)
    #     # self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
    #     self.get_item_input_box().send_keys(Keys.ENTER)

    #     # browser intercepts request, doesn't load the list page
    #     self.wait_for(lambda: self.browser.find_element_by_css_selector('#id_text:invalid'))

    #     # Home page refreshes, then error message pops up
    #     # saying list items cannot be blank
    #     # time.sleep(5)
    #     self.wait_for(lambda: self.assertEqual(
    #     	self.browser.find_element_by_css_selector('.has-error').text, 
    #     	"You can't have an empty list item"
    #     ))

    #     # Mike tries again with some text for items, which now works
    #     # self.browser.find_element_by_id('id_new_item').send_keys('Buy Milk')
    #     self.get_item_input_box().send_keys('Buy Milk')
    #     # self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
    #     self.get_item_input_box().send_keys(Keys.ENTER)
    #     self.wait_for_row_in_list_table('1: Buy Milk')
        
    #     # Then he decides to submit a second blank list item
    #     # self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
    #     self.get_item_input_box().send_keys(Keys.ENTER)

    #     # He should receive a similar warning sa list page
    #     self.wait_for(lambda: self.assertEqual(
    #     	self.browser.find_element_by_css_selector('.has-error').text, 
    #     	"You can't have an empty list item"
    #     ))

    #     # Tapos icocorrect nya ulit by filling some text in
    #     # self.browser.find_element_by_id('id_new_item').send_keys('Drink Red Horse Ice Cold')
    #     self.get_item_input_box().send_keys('Drink Red Horse Ice Cold')
    #     # self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
    #     self.get_item_input_box().send_keys(Keys.ENTER)
    #     self.wait_for_row_in_list_table('1: Buy Milk')
    #     self.wait_for_row_in_list_table('2: Drink Red Horse Ice Cold')

    def test_cannot_add_empty_list_items(self):
        # Mike goes to the home page and accidentally tries to submit
        # an empty list item. He hits ENTER on the empty input box
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys(Keys.ENTER)

        # browser intercepts request, doesn't load the list page
        self.wait_for(lambda: self.browser.find_element_by_css_selector('#id_text:invalid'))

        # mike starts typing some text for the new item and the error disappears
        self.get_item_input_box().send_keys('Buy Milk')
        self.wait_for(lambda: self.browser.find_element_by_css_selector('#id_text:valid'))

        # mike can submit it successfully
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy Milk')

        # Home page refreshes, then error message pops up
        # saying list items cannot be blank
        # time.sleep(5)
        # self.wait_for(lambda: self.assertEqual(
        #     self.browser.find_element_by_css_selector('.has-error').text, 
        #     "You can't have an empty list item"
        # ))

        # Mike tries again with some text for items, which now works
        # self.get_item_input_box().send_keys('Buy Milk')
        # self.get_item_input_box().send_keys(Keys.ENTER)
        # self.wait_for_row_in_list_table('1: Buy Milk')
        
        # Then he decides to submit a second blank list item
        self.get_item_input_box().send_keys(Keys.ENTER)

        # browser again won't comply
        self.wait_for_row_in_list_table('1: Buy Milk')
        self.wait_for(lambda: self.browser.find_element_by_css_selector('#id_text:invalid'))

        # He should receive a similar warning sa list page
        # self.wait_for(lambda: self.assertEqual(
        #     self.browser.find_element_by_css_selector('.has-error').text, 
        #     "You can't have an empty list item"
        # ))

        # Tapos icocorrect nya ulit by filling some text in
        self.get_item_input_box().send_keys('Drink Red Horse Ice Cold')
        self.wait_for(lambda: self.browser.find_element_by_css_selector('#id_text:valid'))
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy Milk')
        self.wait_for_row_in_list_table('2: Drink Red Horse Ice Cold')

    def test_cannot_add_duplicate_items(self):
        # Mike goes to homepage, starts new list
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys('Buy wellies')
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy wellies')

        # Mike accidentally tries to enter a duplicate item
        self.get_item_input_box().send_keys('Buy wellies')
        self.get_item_input_box().send_keys(Keys.ENTER)
        # Mike reads a helpful error message
        self.wait_for(
            lambda: self.assertEqual(
                self.browser.find_element_by_css_selector(
                    '.has-error').text, "You've already got this on your list"))
