from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import CreateView, DetailView, View
from .forms import RegisterForm
from .models import Profile
# get default authenticate backend
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.


# create a function to resolve email to username

# def get_user(email):
#     try:
#         return User.objects.get(email=email.lower())
#     except User.DoesNotExist:
#         return None

# # create a view that authenticate user with email
# def email_login_view(request):
#     email = request.POST.get('email','')
#     password = request.POST.get('password','')
#     username = get_user(email)
#     user = authenticate(username=username, password=password)
#     if user is not None:
#         if user.is_active:
#             login(request, user)
#             print('Redirecting to home')
#             return redirect("/home")
#         else:
#             print('Disabled account.')
#             messages.error(request, 'Disabled account.')

#             # Return a 'disabled account' error message
#     else:
#         print('Invalid login')
#         messages.error(request, 'Invalid login')
#         # Return an 'invalid login' error message.
#     return render(request,'datasheet/index.html')

# class Login_View(LoginRequiredMixin, View):
#     login_url = '/login/'
#     redirect_field_name = 'home'

# def login_view(request):
#     print(request)
#     template_name='registration/login.html'
#     username = request.POST.get('username','')
#     password = request.POST.get('password','')
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         if user.is_active:
#             login(request, user)
#             print('Redirecting to home')
#             return redirect("/home")
#         else:
#             print('Disabled account.')
#             messages.error(request, 'Disabled account.')
#             return redirect(reverse('login'))
#     else:
#         print('Invalid login')
#         print('username:'+username+',password'+password)
#         messages.error(request, 'Invalid login') #appear in admin page
#         return redirect(reverse('home'))
        


class SignupView(SuccessMessageMixin, CreateView):
    form_class = RegisterForm
    template_name = 'registration/signuppage.html'
    success_url = '/login'
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
    template_name="home.html"
    return render(request,template_name)

def pending_activation_view(request):
    template_name='pendingactivation.html'
    return render(request,template_name)





