from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists import templates
from lists.models import Item, List

# home_page = None


def home_page(request):
	"""	if request.method == 'POST': 
		return HttpResponse(request.POST['item_text'])
	else:"""
	# if request.method == 'POST':
	# 	# new_item_text = request.POST.get("item_text",'')
	# 	# Item.objects.create(text=new_item_text)
	# 	Item.objects.create(text=request.POST['item_text'])
	# 	# return redirect('/')
	# 	return redirect('/lists/the-only-list-in-the-world/')
	# else:
		# new_item_text = ""
	# return render(request, 'home.html', {'new_item_text': new_item_text, })

	# items = Item.objects.all()
	# return HttpResponse("<html><title>TO-DO</title></html>")
	# Create your views here.
	return render(request, 'home.html')
	

def view_list(request, foo):
	# items = Item.objects.all()
	list_ = List.objects.get(id=foo)
	return render(request, 'list.html', {'list': list_})


def new_list(request):
	list_ = List.objects.create()
	Item.objects.create(text=request.POST['item_text'], list = list_)
	return redirect(f'/lists/{list_.id}/')

def add_item(request, foo):
	list_ = List.objects.get(id=foo)
	Item.objects.create(text=request.POST['item_text'], list = list_)
	return redirect(f'/lists/{list_.id}/')
