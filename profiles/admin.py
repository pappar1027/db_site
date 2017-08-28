from django.contrib import admin
from .models import Profile, Data_admin, Datasheet_app, Data_access

# Register your models here.

admin.site.register(Profile)
admin.site.register(Datasheet_app)
admin.site.register(Data_admin)
admin.site.register(Data_access)