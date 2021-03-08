from django.shortcuts import render
from django.http import HttpResponse
from lists import templates
# home_page = None


def home_page(request):
	return render(request,'home.html')
	# return HttpResponse("<html><title>TO-DO</title></html>")
# Create your views here.
