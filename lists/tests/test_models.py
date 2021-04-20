from django.test import TestCase
from django.core.exceptions import ValidationError
# from django.urls import resolve
# from lists.views import home_page
# from lists.models import Item
from lists.models import Item, List
# from django.http import HttpRequest
# from django.template.loader import render_to_string

# Create your tests here.
# class SmokeTest(TestCase):
# 	def test_bad_math(self):
# 		self.assertEqual(1+1, 4)


class ItemModelTest(TestCase):
	def test_default_text(self):
		item = Item()
		self.assertEqual(item.text, '')

	def test_item_is_related_to_list(self):
		list_ = List.objects.create()
		item = Item()
		item.list = list_
		item.save()
		self.assertIn(item, list_.item_set.all())

	def test_cannot_save_empty_list_items(self):
		list_ = List.objects.create()
		item = Item(list=list_, text='')
		with self.assertRaises(ValidationError):
			item.save()
			item.full_clean()

	def test_duplicate_items_are_invalid(self):
		list_ = List.objects.create()
		Item.objects.create(list=list_, text='bla')
		with self.assertRaises(ValidationError):
			item = Item(list=list_, text='bla')
			item.full_clean()
			# item.save()

	def test_CAN_save_same_item_to_different_lists(self):
		list1 = List.objects.create()
		list2 = List.objects.create()
		Item.objects.create(list=list1, text='bla')
		item = Item(list=list2, text='bla')
		item.full_clean() # should not raise an error

	def test_list_ordering(self):
		list1 = List.objects.create()
		item1 = Item.objects.create(list=list1, text='i1')
		item2 = Item.objects.create(list=list1, text='item 2')
		item3 = Item.objects.create(list=list1, text='3')
		self.assertEqual(list(Item.objects.all()), [item1, item2, item3])

	def test_string_representation(self):
		item = Item(text='some text')
		self.assertEqual(str(item), 'some text')


# class ItemModelTest(TestCase):
class ListModelTest(TestCase):
	def test_get_absolute_url(self):
		list_ = List.objects.create()
		self.assertEqual(list_.get_absolute_url(), f'/lists/{list_.id}/')

	# def test_saving_and_retrieving_items(self):
	# 	list_ = List()
	# 	list_.save()

	# 	first_item = Item()
	# 	first_item.text = 'The first (ever) list item'
	# 	first_item.list = list_
	# 	first_item.save()

	# 	second_item = Item()
	# 	second_item.text = 'Item the second'
	# 	second_item.list = list_
	# 	second_item.save()

	# 	saved_list = List.objects.first()
	# 	self.assertEqual(saved_list, list_)

	# 	saved_items = Item.objects.all()
	# 	self.assertEqual(saved_items.count(), 2)

	# 	first_saved_item = saved_items[0]
	# 	# print(first_saved_item.text)
	# 	second_saved_item = saved_items[1]
	# 	# print(second_saved_item.text)
	# 	self.assertEqual(first_saved_item.text, 'The first (ever) list item')
	# 	self.assertEqual(first_saved_item.list, list_)
	# 	self.assertEqual(second_saved_item.text, 'Item the second')
	# 	self.assertEqual(second_saved_item.list, list_)

	# def test_default_text(self):
	# 	item = Item()
	# 	self.assertEqual(item.text, '')

	# def test_item_is_related_to_list(self):
	# 	list_ = List.objects.create()
	# 	item = Item()
	# 	item.list = list_
	# 	item.save()
	# 	self.assertIn(item, list_.item_set.all())

	# def test_cannot_save_empty_list_items(self):
	# 	list_ = List.objects.create()
	# 	item = Item(list=list_, text='')
	# 	with self.assertRaises(ValidationError):
	# 		item.save()
	# 		item.full_clean()

	# def test_duplicate_items_are_invalid(self):
	# 	list_ = List.objects.create()
	# 	Item.objects.create(list=list_, text='bla')
	# 	with self.assertRaises(ValidationError):
	# 		item = Item(list=list_, text='bla')
	# 		item.full_clean()

	# def test_CAN_save_same_item_to_different_lists(self):
	# 	list1 = List.objects.create()
	# 	list2 = List.objects.create()
	# 	Item.objects.create(list=list1, text='bla')
	# 	item = Item(list=list2, text='bla')
	# 	item.full_clean() # should not raise an error

	# def test_list_ordering(self):
	# 	list1 = List.objects.create()
	# 	item1 = Item.objects.create(list=list1, text='i1')
	# 	item2 = Item.objects.create(list=list1, text='item 2')
	# 	item3 = Item.objects.create(list=list1, text='3')
	# 	self.assertEqual(list(Item.objects.all()), [item1, item2, item3])

	# def test_string_representation(self):
	# 	item = Item(text='some text')
	# 	self.assertEqual(str(item), 'some text')


# class HomePageTest(TestCase):
# 	def test_root_url_resolution_to_home_page_view(self):
# 		found = resolve('/')
# 		self.assertEqual(found.func, home_page)

# 	# def test_home_page_returns_correct_html(self):
# 	# 	# request = HttpRequest()
# 	# 	response = self.client.get('/')
# 	# 	# html = response.content.decode('utf8')
# 	# 	# self.assertTrue(html.startswith('<html>'))
# 	# 	# self.assertIn('<title>To-Do lists</title>', html)
# 	# 	# self.assertTrue(html.strip().endswith('</html>'))
# 	# 	self.assertTemplateUsed(response, 'home.html')
# 	# 	# expected_html = render_to_string('home.html')
# 	# 	# self.assertEqual(html, expected_html)

# 	def test_uses_home_template(self):
# 		response = self.client.get('/')
# 		self.assertTemplateUsed(response, 'home.html')

	# # since it is moved in the new list
	# def test_can_save_a_POST_request(self):
	# 	# response = self.client.post('/', data={'item_text': 'A new list item'}) # form data to send
	# 	self.client.post('/', data={'item_text': 'A new list item'}) # form data to send
		
	# 	self.assertEqual(Item.objects.count(), 1)
	# 	new_item = Item.objects.first()
	# 	self.assertEqual(new_item.text, 'A new list item')
		
	# 	# self.assertIn('A new list item', response.content.decode())
	# 	# self.assertTemplateUsed(response, 'home.html')

	# 	# self.assertEqual(response.status_code, 302)
	# 	# self.assertEqual(response['location'], '/')

	# def test_redirects_after_POST(self):  # initial invocation of the URL
	# 	response = self.client.post('/', data={'item_text': 'A new list item'})

	# 	self.assertEqual(response.status_code, 302)
	# 	# self.assertEqual(response['location'], '/')
	# 	self.assertEqual(response['location'], '/lists/the-only-list-in-the-world/')

	# def test_only_saves_items_when_needed(self):
	# 	self.client.get('/')
	# 	self.assertEqual(Item.objects.count(), 0)

	# no longer needed
	# def test_displays_all_list_items(self):
	# 	Item.objects.create(text='itemey 1')
	# 	Item.objects.create(text='itemey 2')

	# 	response = self.client.get('/')
		
	# 	self.assertIn('itemey 1', response.content.decode())
	# 	self.assertIn('itemey 2', response.content.decode())

# class ListViewTest(TestCase):
# 	def test_uses_list_template(self):
# 		list_ = List.objects.create()
# 		# response = self.client.get('/lists/the-only-list-in-the-world/')
# 		response = self.client.get(f'/lists/{list_.id}/')
# 		self.assertTemplateUsed(response, 'list.html')

# 	# def test_displays_all_list_items(self):
# 	# 	list_ = List.objects.create()
# 	# 	Item.objects.create(text='itemey 1', list=list_)
# 	# 	Item.objects.create(text='itemey 2', list=list_)

# 	# 	response = self.client.get('/lists/the-only-list-in-the-world/')
		
# 	# 	# self.assertIn('itemey 1', response.content.decode())
# 	# 	# self.assertIn('itemey 2', response.content.decode())
# 	# 	self.assertContains(response, 'itemey 1')
# 	# 	self.assertContains(response, 'itemey 2')

# 	def test_displays_only_items_for_that_list(self):
# 		correct_list = List.objects.create()
# 		Item.objects.create(text='itemey 1', list=correct_list)
# 		Item.objects.create(text='itemey 2', list=correct_list)

# 		other_list = List.objects.create()
# 		Item.objects.create(text='string 1', list=other_list)
# 		Item.objects.create(text='string 2', list=other_list)

# 		response = self.client.get(f'/lists/{correct_list.id}/')

# 		self.assertContains(response, 'itemey 1')
# 		self.assertContains(response, 'itemey 2')
# 		self.assertNotContains(response, 'string 1')
# 		self.assertNotContains(response, 'string 2')

# 	def test_passes_correct_list_to_template(self):
# 		other_list = List.objects.create()
# 		correct_list = List.objects.create()

# 		response = self.client.get(f'/lists/{correct_list.id}/')
# 		self.assertEqual(response.context['list'], correct_list)

# class NewListTest(TestCase):
# 	def test_can_save_a_POST_request(self):
# 		self.client.post('/lists/new', data={'item_text': 'A new list item'})
		
# 		self.assertEqual(Item.objects.count(), 1)
# 		new_item = Item.objects.first()
# 		self.assertEqual(new_item.text, 'A new list item')

# 	def test_redirects_after_POST(self):
# 		response = self.client.post('/lists/new', data={'item_text': 'A new list item'})
# 		new_list = List.objects.first()
# 		# self.assertEqual(response.status_code, 302)
# 		# self.assertEqual(response['location'], '/lists/the-only-list-in-the-world/')
# 		# self.assertRedirects(response, '/lists/the-only-list-in-the-world/') # shortcut of 114-115
# 		self.assertRedirects(response, f'/lists/{new_list.id}/') # shortcut of 114-115

# class NewItemTest(TestCase):
# 	def test_can_save_a_POST_request_to_an_existing_list(self):
# 		other_list = List.objects.create()
# 		correct_list = List.objects.create()

# 		self.client.post(f'/lists/{correct_list.id}/add_item', data={'item_text': 'A new item for the created list'})
		
# 		self.assertEqual(Item.objects.count(), 1)
# 		new_item = Item.objects.first()
# 		self.assertEqual(new_item.text, 'A new item for the created list')
# 		self.assertEqual(new_item.list, correct_list)

# 	def test_redirects_to_list_view(self):
# 		other_list = List.objects.create()
# 		correct_list = List.objects.create()

# 		response = self.client.post(f'/lists/{correct_list.id}/add_item', data={'item_text': 'A new item for the created list'})
# 		self.assertRedirects(response, f'/lists/{correct_list.id}/')
