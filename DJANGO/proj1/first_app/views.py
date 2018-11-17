from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    # return HttpResponse("<h1>Hello World!</h1>")
		my_dict = {'insert_me': "Hello, I'm inserted"}
		return render(request, 'first_app/index.html', context=my_dict)