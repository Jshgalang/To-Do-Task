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
		# code smell

	def test_uses_home_page_template(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'home.html')

	def test_can_save_a_POST_request(self):
		self.client.post('/', data={'item_text': 'A new list item'}) # form data to send

		self.assertEqual(Item.objects.count(), 1) # short for objects.all().count()
		new_item = Item.objects.first()
		self.assertEqual(new_item.text, 'A new list item')

		# self.assertIn('A new list item', response.content.decode())
		# self.assertTemplateUsed(response, 'home.html')

	def test_only_saves_items_when_needed(self):
		self.client.get('/')
		self.assertEqual(Item.objects.count(),0)

	def test_redirects_after_POST(self):
		response = self.client.post('/', data={'item_text': 'A new list item'})
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response['location'], '/')

	def test_displays_all_list_items(self):
		Item.objects.create(text='itemey 1')
		Item.objects.create(text='itemey 2')
		response = self.client.get('/')
		self.assertIn('itemey 1', response.content.decode())
		self.assertIn('itemey 2', response.content.decode())


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