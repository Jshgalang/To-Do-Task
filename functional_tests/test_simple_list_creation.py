# import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# from django.test import LiveServerTestCase
# from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.common.exceptions import WebDriverException
# from unittest import skip
from base import FunctionalTest

MAX_WAIT = 10 # catch random glitches / random slowdowns


class MikeTest(FunctionalTest):
    """def test_start_a_list_and_retrieve_it_later(self):  # good for 1 user only
                    # self.browser.get('http://localhost:8000')
                    self.browser.get(self.live_server_url) #from LiveServerTestCase
                    self.assertIn('To-Do', self.browser.title)
                    header_text = self.browser.find_element_by_tag_name('h1').text # user types into the textbox
                    self.assertIn('Start a new To-Do List', header_text)
            
                    inputbox = self.browser.find_element_by_id('id_new_item')
                    self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a to-do item:') 
                    inputbox.send_keys('Mike will eat a meatball') # enable the user to insert an entry
                    inputbox.send_keys(Keys.ENTER)
                    # time.sleep(1) # not needed anymore after adding the wait function
            
                    # self.check_for_row_in_list_table('1: Mike will eat a meatball')
                    self.wait_for_row_in_list_table('1: Mike will eat a meatball')
            
                    inputbox = self.browser.find_element_by_id('id_new_item')
                    inputbox.send_keys('Mike will digest the meatball') # enable the user to insert an entry
                    inputbox.send_keys(Keys.ENTER)
                    # time.sleep(1) # not needed anymore after adding the wait function
            
                    # page updates and reflects content of textbox after entering
                    # self.check_for_row_in_list_table('1: Mike will eat a meatball')
                    # self.check_for_row_in_list_table('2: Mike will digest the meatball')
                    self.wait_for_row_in_list_table('1: Mike will eat a meatball')
                    self.wait_for_row_in_list_table('2: Mike will digest the meatball') 
                # multipleuserscanstartlistsatdiffurls
                
                def test_add_entry_and_retrieve_later(self):
                    self.browser.get(self.live_server_url)
                    self.assertIn('To-Do', self.browser.title, f'Browser title was {self.browser.title}')
                    # self.fail('Finish the Test')
            
                    """
    def test_multiple_users_can_start_lists_at_different_urls(self):
        # Mike starts a new to do list
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Mike will eat a meatball')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Mike will eat a meatball')
        # wait
        mike_list_url = self.browser.current_url
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertRegex(mike_list_url, '/lists/.+') # check that other users don't see mike's list and that they each have unique URLs
        """
        assuming we have new users, we check that they dont see mike's list AND that they each have unique URLs

        """

        self.browser.quit() # new browser session
        self.browser = webdriver.Firefox()

        # Iso visits home page. No sign of Mike's list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Mike will eat a meatball', page_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk') 
        inputbox.send_keys(Keys.ENTER)

        self.wait_for_row_in_list_table('1: Buy milk')
        iso_list_url = self.browser.current_url # Iso gets her own unique URL
        self.assertRegex(iso_list_url, '/lists/.+') # No trace of Mike's list dapat
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Mike will eat a meatball', page_text)
