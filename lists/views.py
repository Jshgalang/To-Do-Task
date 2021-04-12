from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from lists import templates
from lists.models import Item, List

# home_page = None


def home_page(request):
	return render(request, 'home.html')
	

def view_list(request, foo):
	# items = Item.objects.all()
	list_ = List.objects.get(id=foo)
	error = None
	if request.method == 'POST':
		try:
			item = Item(text=request.POST['item_text'], list=list_)
			item.full_clean()
			item.save()
			return redirect(f'/lists/{list_.id}/')
		except ValidationError:
			error = "You can't have an empty list item"
			# return render(request, 'list.html', {'list': list_, 'error': error})
	return render(request, 'list.html', {'list': list_, 'error': error})


def new_list(request):
	list_ = List.objects.create()
	item = Item.objects.create(text=request.POST['item_text'], list = list_)
	try:
		item.full_clean()
		item.save()
	except ValidationError:
		list_.delete()
		error = "You can't have an empty list item"
		return render(request, 'home.html', {'error': error})
	return redirect(f'/lists/{list_.id}/')

# def add_item(request, foo):
# 	list_ = List.objects.get(id=foo)
# 	Item.objects.create(text=request.POST['item_text'], list = list_)
# 	return redirect(f'/lists/{list_.id}/')
# not needed anymore because added to view_list