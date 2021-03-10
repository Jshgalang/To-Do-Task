from django.shortcuts import render, redirect
from lists.models import Item
# from django.http import HttpResponse

# Create your views here.
# home_page = None

def home_page(request):
	# return HttpResponse('<html>')
	# return HttpResponse('<html><title>To-Do lists</title>')
	# return HttpResponse('<html><title>To-Do lists</title></html>')
	# if request.method == 'POST':
	# 	return HttpResponse(request.POST['item_text'])

	if request.method == 'POST':
		# new_item_text = request.POST['item_text']
		# Item.objects.create(text=new_item_text)
		Item.objects.create(text=request.POST['item_text'])
		return redirect('/')
	# else:
	# 	new_item_text = ''

	# item = Item()
	# item.text = request.POST.get('item_text', '')
	# item.save() 
	# return render(request, 'home.html', {'new_item_text': new_item_text, })
	items = Item.objects.all()
	return render(request, 'home.html', {'items': items})
