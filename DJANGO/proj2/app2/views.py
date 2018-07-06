from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def help(request):
	# return HttpResponse("<em>My Second App</em>")
	dict1 = {'main_header': "HELP!!!"}
	return render(request, "app2/help.html", context=dict1)

def index(request): 
	return render(request, "index.html")