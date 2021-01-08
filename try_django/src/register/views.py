from django.shortcuts import render , redirect
from .forms import *
from django.core.mail import send_mail
import random
from django.conf import *
# Create your views here.

#  https://stackoverflow.com/questions/53594745/what-is-the-use-of-cleaned-data-in-django

class otpGenerator():
    def __init__(self):
        self.otp = str(random.randint(9999,100000))
        self.subject = "Rebuild your password using this OTP {0}".format(self.otp)
        self.message = "don't share this email"
        self.email_from = settings.EMAIL_HOST_USER
        self.recipient_list = []

    def generate(self,recipients):
        self.recipient_list = recipients
        send_mail(self.subject,self.message,self.email_from,self.recipient_list)
        return self.otp

def register(request):
    if response.method =="POST":
        form = RegistrationForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/home")
    else:
        form = RegistrationForm()
    context = {"form" : form }
    return render(request,"register/register.html", context)



def forget(request):
    form =  OtpEmail(request.POST or None)
    if form.is_valid() :
        recipient_list = [request.POST["Email"],]
        otp = otp_obj.generate(recipient_list)
        # print(form.cleaned_data)
        # context = {"form" : form.OTP}
        return redirect("/enterotp/")
    context = {"form" : form}
    return render(request,"registration/forget.html",context)

def EnterOtp(request):
    form = OtpForm(request.POST or None)
    if form.is_valid() and  request.POST["OTP"] == otp_obj.otp:
        # print("otp_obj = ",otp_obj.otp,"otp = ",otp,"request.POST",request.POST["OTP"])
        # if request.POST["OTP"] == otp_obj.otp:
        print("change password")
        return redirect("/home")
    else:
        form = OtpForm()
    context = {"form" : form }
    return render(request, "registration/enterotp.html",context)

otp_obj = otpGenerator()
otp=0
