from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# home_page = None

def home_page(request):
	# return HttpResponse('<html>')
	# return HttpResponse('<html><title>To-Do lists</title>')
	# return HttpResponse('<html><title>To-Do lists</title></html>')
	return render(request, 'home.html')
