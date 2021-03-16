from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists import templates
from lists.models import Item
# home_page = None


def home_page(request):
	"""	if request.method == 'POST': 
		return HttpResponse(request.POST['item_text'])
	else:"""
	if request.method == 'POST':
		# new_item_text = request.POST.get("item_text",'')
		# Item.objects.create(text=new_item_text)
		Item.objects.create(text=request.POST['item_text'])
		# return redirect('/')
		return redirect('/lists/the-only-list-in-the-world/')
	# else:
		# new_item_text = ""
	# return render(request, 'home.html', {'new_item_text': new_item_text, })

	items = Item.objects.all()
	return render(request, 'home.html', {'items': items})
	# return HttpResponse("<html><title>TO-DO</title></html>")
	# Create your views here.

def view_list(request):
	items = Item.objects.all()
	return render(request, 'home.html', {'items': items})