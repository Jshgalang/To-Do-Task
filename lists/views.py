from django.shortcuts import render
from django.http import HttpResponse
from lists import templates
# home_page = None


def home_page(request):
	"""	if request.method == 'POST': 
		return HttpResponse(request.POST['item_text'])
	else:"""
	return render(request,'home.html', {'new_item_text': request.POST.get("item_text",''), })
	# return HttpResponse("<html><title>TO-DO</title></html>")
# Create your views here.
