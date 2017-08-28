"""db_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from profiles.views import SignupView, activate_user_view, home_view, login_view, pending_activation_view
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
	url(r'^datasheet/', include('datasheet.urls')), #include-->sends the remaining string to the included URLconf for further processing
	url(r'^signup/$', SignupView.as_view(), name='signup'),
	url(r'^activate/(?P<code>[a-z0-9].*)/$', activate_user_view, name='activate'),
	url(r'^pending_activation/$', pending_activation_view, name='pending_activation'),
	url(r'^login/$', LoginView.as_view(), name='login'),
	url(r'^home/$',home_view, name='home'),
    url(r'^admin/', admin.site.urls),

]
