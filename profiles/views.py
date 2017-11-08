from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import CreateView, DetailView, View
from .forms import RegisterForm
from .models import Profile, Data_admin, Data_access, Datasheet_app
# get default authenticate backend
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import QueryDict
# Create your views here.



        


class SignupView(SuccessMessageMixin, CreateView):
    form_class = RegisterForm
    template_name = 'registration/signuppage.html'
    success_url = '/pending_activation'
    success_message = "Your account was created successfully. Please check your email."

    def dispatch(self, *args, **kwargs):
        # if self.request.user.is_authenticated():
        #     return redirect("/logout")
        return super(SignupView, self).dispatch(*args, **kwargs)

def activate_user_view(request, code=None, *args, **kwargs):
    if code:
        qs = Profile.objects.filter(activation_key=code)
        if qs.exists() and qs.count() == 1:
            profile = qs.first()
            if not profile.activated:
                user_ = profile.user
                user_.is_active = True
                user_.save()
                profile.activated=True
                profile.activation_key=None
                profile.save()
                return redirect("/login")
    return redirect("/login")

def home_view(request):
    if request.user.is_active:
        print(request.META)
        
        if 'HTTP_X_METHODOVERRIDE' in request.META:
            print('yay')
            http_method=request.META['HTTP_X_METHODOVERRIDE']
            if http_method.lower() == 'delete':
                request.method = 'DELETE'
                request.META['REQUEST_METHOD'] = 'DELETE'
                request.DELETE = QueryDict(request.body)
        if request.method=='DELETE':
            datasheet_name_to_remove=request.DELETE['datasheet_name']
            user_name_to_remove=request.DELETE['user_name']
            datasheet_app_chosen=Datasheet_app.objects.get(datasheet_name=datasheet_name_to_remove)
            data_access_to_remove=Data_access.objects.get(datasheet_name=datasheet_app_chosen,user_name=user_name_to_remove)
            data_access_to_remove.delete()

        # elif 'HTTP_X_CHOOSE' in request.META:

        #     datasheet_chosen = request.POST['datasheet_name']
        #     datasheet_name=Datasheet_app.objects.filter(datasheet_name=datasheet_chosen)
        #     context['data_chosen'] = Data_access.objects.filter(datasheet_name=datasheet_name)

        elif request.method=='POST' and 'datasheet_admin_name' not in request.POST:
            new_datasheet_name=request.POST['datasheet_name']
            new_datasheet_app=Datasheet_app.objects.get(datasheet_name=new_datasheet_name)
            new_user_name=request.POST['user_name']
            new_entry=Data_access.objects.get_or_create(
            datasheet_name=new_datasheet_app,
            user_name=new_user_name
            )

        username=request.user.get_username()
        data_access=Data_access.objects.filter(user_name=username)
        data_admin=Data_admin.objects.filter(admin_name=username)
        data_access_qs_total=Data_access.objects.none()
        for data_admin_entry in data_admin:
            datasheet_app=data_admin_entry.datasheet_name
            data_access_qs=Data_access.objects.filter(datasheet_name=datasheet_app)
            data_access_qs_total=data_access_qs_total | data_access_qs

        
        if 'datasheet_admin_name' in request.POST:
            datasheet_chosen = request.POST['datasheet_admin_name']
            datasheet_name=Datasheet_app.objects.filter(datasheet_name=datasheet_chosen)
            data_access_qs_total = Data_access.objects.filter(datasheet_name=datasheet_name)
            

        context=dict(username=username,data_access=data_access,data_admin_all=data_admin, data_chosen=data_access_qs_total)

            



    template_name="home.html"

    return render(request,template_name,context)

def pending_activation_view(request):
    template_name='pendingactivation.html'
    return render(request,template_name)





