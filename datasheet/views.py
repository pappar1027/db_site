from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login


# Create your views here.


def index(request):
	number_list=[20,20.6,7]
	context={'contentlist':number_list}
	template_name="datasheet/index.html"
	return render(request,template_name,context)
