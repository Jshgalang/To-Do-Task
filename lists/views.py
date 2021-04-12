from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from lists.models import Item, List
# from django.http import HttpResponse

# Create your views here.
# home_page = None

# homepage controller
def home_page(request):
	# return HttpResponse('<html>')
	# return HttpResponse('<html><title>To-Do lists</title>')
	# return HttpResponse('<html><title>To-Do lists</title></html>')
	# if request.method == 'POST':
	# 	return HttpResponse(request.POST['item_text'])

	# # not needed because it has delegated its own controller
	# if request.method == 'POST':
	# 	# new_item_text = request.POST['item_text']
	# 	# Item.objects.create(text=new_item_text)
	# 	Item.objects.create(text=request.POST['item_text'])
	# 	# return redirect('/')
	# 	return redirect('/lists/the-only-list-in-the-world/')
	
	# else:
	# 	new_item_text = ''

	# item = Item()
	# item.text = request.POST.get('item_text', '')
	# item.save() 
	# return render(request, 'home.html', {'new_item_text': new_item_text, })
	
	# items = Item.objects.all()
	# return render(request, 'home.html', {'items': items})
	return render(request, 'home.html')

# list controller
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
			# return render(request, 'list.html', {'list': list_,'error': error})
	return render(request, 'list.html', {'list': list_,'error': error})
		# Item.objects.create(text=request.POST['item_text'], list=list_)
		# return redirect(f'/lists/{list_.id}/')
	# return render(request, 'list.html', {'list': list_})

def new_list(request):
	list_ = List.objects.create()
	item = Item.objects.create(text=request.POST['item_text'], list=list_)
	# item.full_clean()
	try:
		item.full_clean()
		item.save()
	except ValidationError:
		list_.delete()
		error = "You can't have an empty list item" 
		return render(request, 'home.html', {"error": error})
	return redirect(f'/lists/{list_.id}/')

# def add_item(request, foo):
# 	list_ = List.objects.get(id=foo)
# 	Item.objects.create(text=request.POST['item_text'], list=list_)
# 	return redirect(f'/lists/{list_.id}/')