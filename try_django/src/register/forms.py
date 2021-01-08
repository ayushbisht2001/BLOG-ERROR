from django import forms
from django.contrib.auth import login , authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import re
from captcha.fields import CaptchaField
import random
from django.conf import *

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    captcha =CaptchaField()

    class Meta:
        model = User
        fields = ["username" , "email" , "password1" , "password2",'captcha']

    def clean_email(self,*args,**kwargs):
        instance = self.instance
        email= self.cleaned_data.get("email")
        valid_email = "@gmail.com\Z"
         # title__iexact :  it basically ignore the case-sensitivity  ;  title = lower(title)
        if not re.findall(valid_email,email):
            raise forms.ValidationError("Enter the correct email address ")
        return email

    def clean_captcha(self,*args,**kwargs):
        instance = self.instance
        print("hello ayush")
        captcha = self.cleaned_data.get("captcha")
        print(valid_captcha , "hello world ")
        return captcha


class OtpEmail(forms.Form):
    Email  = forms.EmailField()
    class Meta:
        fields = ["Email"]

class OtpForm(forms.Form):
    OTP = forms.CharField()
    class Meta:
        fields = ["OTP"]
