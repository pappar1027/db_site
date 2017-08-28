from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .models import Option
from .utils import get_web_data 

# Create your views here.


def index(request,data_type=None):
	# get_web_data()
	print(data_type)
	if data_type is None:
		options=Option.objects.all()
	else:
		options=Option.objects.filter(calls_or_puts=data_type)
	context={'contentlist':options}
	template_name="datasheet/index.html"
	return render(request,template_name,context)


# def index_search(request):
# 	# get_web_data()
# 	if data_type is None:
# 		options=Option.objects.all()
# 	else:
# 		options=Option.objects.filter(calls_or_puts=data_type)
# 	context={'contentlist':options}
# 	template_name="datasheet/index.html"
# 	return render(request,template_name,context)

