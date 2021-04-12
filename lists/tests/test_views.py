from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string
# from lists.models import Item
from lists.models import Item, List
from django.utils.html import escape


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

	# def test_can_save_a_POST_request(self):
	# 	self.client.post('/', data={'item_text': 'A new list item'}) # form data to send

	# 	self.assertEqual(Item.objects.count(), 1) # short for objects.all().count()
	# 	new_item = Item.objects.first()
	# 	self.assertEqual(new_item.text, 'A new list item')

	# 	# self.assertIn('A new list item', response.content.decode())
	# 	# self.assertTemplateUsed(response, 'home.html')

	# def test_only_saves_items_when_needed(self):
	# 	self.client.get('/')
	# 	self.assertEqual(Item.objects.count(),0)

	# def test_redirects_after_POST(self):
	# 	response = self.client.post('/', data={'item_text': 'A new list item'})
	# 	self.assertEqual(response.status_code, 302) # This is where we get the URLs
	# 	# self.assertEqual(response['location'], '/')
	# 	self.assertEqual(response['location'], '/lists/the-only-list-in-the-world/') #
	"""
	def test_displays_all_list_items(self):
		Item.objects.create(text='itemey 1')
		Item.objects.create(text='itemey 2')
		response = self.client.get('/')
		self.assertIn('itemey 1', response.content.decode())
		self.assertIn('itemey 2', response.content.decode())
	"""


class ListViewTest(TestCase):
	def test_uses_list_template(self):
		list_ = List.objects.create()
		response = self.client.get(f'/lists/{list_.id}/')
		self.assertTemplateUsed(response, 'list.html')

	# def test_displays_all_list_items(self):
	# 	list_ = List.objects.create()
	# 	Item.objects.create(text='itemey 1', list= list_)
	# 	Item.objects.create(text='itemey 2', list= list_)
	# 	response = self.client.get('/lists/the-only-list-in-the-world/')
	# 	# self.assertIn('itemey 1', response.content.decode())
	# 	# self.assertIn('itemey 2', response.content.decode())
	# 	self.assertContains(response,'itemey 1')
	# 	self.assertContains(response, 'itemey 2')

	def test_displays_only_items_from_that_list(self):
		correct_list = List.objects.create()
		Item.objects.create(text='itemey 1', list=correct_list)
		Item.objects.create(text='itemey 2', list=correct_list)

		other_list = List.objects.create()
		Item.objects.create(text='iso 1', list=other_list)
		Item.objects.create(text='iso 2', list=other_list)

		# self.assertIn('itemey 1', response.content.decode())
		# self.assertIn('itemey 2', response.content.decode())
		print(f'lists/{correct_list.id}/')
		response = self.client.get(f'/lists/{correct_list.id}/')

		self.assertContains(response,'itemey 1')
		self.assertContains(response, 'itemey 2')
		self.assertNotContains(response,'iso 1')
		self.assertNotContains(response, 'iso 2')


	def test_can_save_a_POST_request_to_an_existing_list(self):
		other_list = List.objects.create()
		correct_list = List.objects.create()

		self.client.post(f'/lists/{correct_list.id}/', data={'item_text': 'A new item for the created list'})
		
		self.assertEqual(Item.objects.count(), 1)
		new_item = Item.objects.first()
		self.assertEqual(new_item.text, 'A new item for the created list')
		self.assertEqual(new_item.list, correct_list)

	def test_POST_redirects_to_list_view(self):
		other_list = List.objects.create()
		correct_list = List.objects.create()
		response = self.client.post(f'/lists/{correct_list.id}/', data={'item_text': 'A new item for the created list'})
		self.assertRedirects(response, f'/lists/{correct_list.id}/')
	
	def test_validation_errors_end_up_on_lists_page(self):
 		list_ = List.objects.create()
 		response = self.client.post(f'/lists/{list_.id}/', data={'item_text':''})
 		self.assertEqual(response.status_code, 200)
 		expected_error = escape("You can't have an empty list item")
 		# print(response.content.decode())
 		self.assertContains(response, expected_error)


class NewListTest(TestCase):
	def test_can_save_a_POST_request(self):
		self.client.post('/lists/new', data={'item_text': 'A new list item'}) # form data to send

		self.assertEqual(Item.objects.count(), 1) # short for objects.all().count()
		new_item = Item.objects.first()
		self.assertEqual(new_item.text, 'A new list item')

	def test_redirects_after_POST(self):
		response = self.client.post('/lists/new', data={'item_text': 'A new list item'})
		new_list = List.objects.first()
		self.assertRedirects(response, f'/lists/{new_list.id}/')
		# self.assertEqual(response.status_code, 302) # This is where we get the URLs
		# self.assertEqual(response['location'], '/')
		# self.assertEqual(response['location'], '/lists/the-only-list-in-the-world/')

	def test_validation_errors_are_sent_back_to_home_page_template(self):
		# refactor repeated hardcoded urls /lists/view.py
		response = self.client.post('/lists/new', data={'item_text': ''}) # to be refactored
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'home.html')
		expected_error = escape("You can't have an empty list item")
		# print(response.content.decode())
		self.assertContains(response, expected_error)

	def test_invalid_list_items_arent_saved(self):
		response = self.client.post('/lists/new', data={'item_text': ''})
		self.assertEqual(List.objects.count(), 0)
		self.assertEqual(Item.objects.count(), 0)




# class NewItemTest(TestCase):
# 	def test_can_save_a_POST_request_to_an_existing_list(self):
# 		other_list = List.objects.create()
# 		correct_list = List.objects.create()

# 		self.client.post(f'/lists/{correct_list.id}/add_item', data={'item_text': 'A new item for the created list'})
		
# 		self.assertEqual(Item.objects.count(), 1)
# 		new_item = Item.objects.first()
# 		self.assertEqual(new_item.text, 'A new item for the created list')
# 		self.assertEqual(new_item.list, correct_list)

# 	def test_POST_redirects_to_list_view(self):
# 		other_list = List.objects.create()
# 		correct_list = List.objects.create()

# 		response = self.client.post(f'/lists/{correct_list.id}/add_item', data={'item_text': 'A new item for the created list'})
# 		self.assertRedirects(response, f'/lists/{correct_list.id}/')


	# def test_can_save_a_POST_request_to_an_existing_list(self):
	# 	other_list = List.objects.create()
	# 	correct_list = List.objects.create()

	# 	self.client.post(f'/lists/{correct_list.id}/add_item', data={'item_text': 'A new item for the created list'})
		
	# 	self.assertEqual(Item.objects.count(), 1)
	# 	new_item = Item.objects.first()
	# 	self.assertEqual(new_item.text, 'A new item for the created list')
	# 	self.assertEqual(new_item.list, correct_list)

	# def test_redirects_to_list_view(self):
	# 	other_list = List.objects.create()
	# 	correct_list = List.objects.create()

	# 	response = self.client.post(f'/lists/{correct_list.id}/add_item', data={'item_text': 'A new item for the created list'})
	# 	self.assertRedirects(response, f'/lists/{correct_list.id}/')

"""
# class SmokeTest(TestCase):
	# def test_bad_math(self):
		# self.assertEqual(1+1, 4)
# Create your tests here.
"""