from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from lists import templates
from lists.models import Item, List
from lists.forms import ItemForm, EMPTY_ITEM_ERROR
# home_page = None


def home_page(request):
	return render(request, 'home.html', {'form': ItemForm()})
	

def view_list(request, foo):
	# items = Item.objects.all()
	list_ = List.objects.get(id=foo)
	form = ItemForm()
	if request.method == 'POST':
		form = ItemForm(data=request.POST)
		if form.is_valid():
			Item.objects.create(text=request.POST['text'], list = list_)
			return redirect(list_)
	return render(request, 'list.html', {'list': list_, 'form': form})


def new_list(request):
	form = ItemForm(data=request.POST)
	if form.is_valid():
		list_ = List.objects.create()
		Item.objects.create(text=request.POST['text'], list = list_)
		return redirect(list_)
	else:
		return render(request, 'home.html', {'form': form})
	# return redirect(f'/lists/{list_.id}/')
	# item = Item.objects.create(text=request.POST['text'], list = list_)
	# try:
	# 	item.full_clean()
	# 	item.save()
	# except ValidationError:
	# 	list_.delete()
	# 	error = EMPTY_ITEM_ERROR

	# 	return render(request, 'home.html', {'form': ItemForm(), 'error': error})
	# # return redirect(f'/lists/{list_.id}/')
	# return redirect(list_)

# def add_item(request, foo):
# 	list_ = List.objects.get(id=foo)
# 	Item.objects.create(text=request.POST['text'], list = list_)
# 	return redirect(f'/lists/{list_.id}/')
# not needed anymore because added to view_list