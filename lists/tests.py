from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.models import Item

class HomePageTest(TestCase):
	def test_root_url_resolution_to_home_page_view(self):
		found = resolve("/")
		self.assertEqual(found.func, home_page)

	# def test_home_page_returns_correct_html(self):
		# request = HttpRequest()
		# response = home_page(request)
		# html = response.content.decode('utf8')
		# self.assertTrue(html.strip().startswith('<html>'))
		# self.assertIn('<title>TO-DO</title>', html)
		# self.assertTrue(html.strip().endswith('</html>'))
		# expected_html = render_to_string("home.html")
		# self.assertEqual(html,expected_html)

	def test_uses_home_page_template(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'home.html')

	def test_can_save_a_POST_request(self):
		response = self.client.post('/', data={'item_text': 'A new list item'}) # form data to send
		self.assertIn('A new list item', response.content.decode())
		self.assertTemplateUsed(response, 'home.html')


class ItemModelTest(TestCase):
	def test_saving_and_retrieving_items(self):
		first_item = Item()
		first_item.text = 'The first (ever) list item'
		first_item.save()

		second_item = Item()
		second_item.text = 'Item the secoond'
		second_item.save()
		
		saved_items = Item.objects.all()
		first_saved_item = saved_items[0]
		second_saved_item = saved_items[1]

		self.assertEqual(first_saved_item.text, 'The first (ever) list item')
		self.assertEqual(second_saved_item.text, 'Item the secoond')
		



"""
class SmokeTest(TestCase):
	def test_bad_math(self):
		self.assertEqual(1+1, 4)
# Create your tests here.
"""