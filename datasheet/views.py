from django.shortcuts import render
from django.http import HttpResponse,HttpResponseForbidden
from django.contrib.auth import authenticate, login
from .models import Option
from .utils import get_web_data, process_data_change
import json

# Create your views here.


def index(request,data_type=None):
	if request.user.is_active:
		if 'HTTP_X_UPDATE' in request.META:
			get_web_data()
		elif request.method=='POST':
			result = json.loads(request.POST['data_changed'])
			for data_entry in result:
				process_data_change(data_entry)
		if data_type is None:
			options=Option.objects.all()
		else:
			options=Option.objects.filter(calls_or_puts=data_type)
		context={'contentlist':options}
		template_name="datasheet/index.html"
		return render(request,template_name,context)
	else:
		return HttpResponseForbidden()

	




