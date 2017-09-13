from django.db import models
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from .utils import code_generator
from django.conf import settings

# Create your models here.

User = settings.AUTH_USER_MODEL

class Profile(models.Model):
    user              = models.OneToOneField(User, primary_key=True) # user.profile
    activation_key    = models.CharField(max_length=120, blank=True, null=True)
    activated         = models.BooleanField(default=False)
    timestamp         = models.DateTimeField(auto_now_add=True)
    updated           = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.user.email

    def send_activation_email(self):
        if not self.activated:
            self.activation_key = code_generator()# 'somekey' #gen key

            self.save()
            #path_ = reverse()
            path_ = reverse('activate', kwargs={"code": self.activation_key})
            full_path = "http://127.0.0.1:8000" + path_
            subject = 'Activate Account'
            from_email = settings.DEFAULT_FROM_EMAIL
            message = f'Activate your account here: {full_path}'
            recipient_list = [self.user.email]
            html_message = f'<p>Activate your account here: {full_path}</p>'
            print(html_message)
            sent_mail = send_mail(
                            subject, 
                            message, 
                            from_email, 
                            recipient_list, 
                            fail_silently=False, 
                            html_message=html_message)
            sent_mail = False
            return sent_mail

class Datasheet_app(models.Model):
    datasheet_name=models.CharField(max_length=120)
    def __str__(self):
        return self.datasheet_name

    @classmethod
    def create(cls, datasheet_name):
        datasheet_app= cls(datasheet_name=datasheet_name)
        return datasheet_app

class Data_admin(models.Model):
    admin_name      =models.CharField(max_length=120, default='')
    datasheet_name  =models.ForeignKey(Datasheet_app,on_delete=models.CASCADE)

    class Meta:
        ordering = ('datasheet_name',)
    def __str__(self):
        return "%s (%s)" %(self.datasheet_name,self.admin_name)

class Data_access(models.Model):
    user_name      =models.CharField(max_length=120, default='')
    datasheet_name  =models.ForeignKey(Datasheet_app,on_delete=models.CASCADE)

    class Meta:
        ordering = ('datasheet_name',)
    def __str__(self):
        return "%s (%s)" %(self.datasheet_name,self.user_name)


