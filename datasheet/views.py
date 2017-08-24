from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .models import Option
from .utils import get_web_data 

# Create your views here.


def index(request):
	
	options=Option.objects.all()
	context={'contentlist':options}
	template_name="datasheet/index.html"
	return render(request,template_name,context)

