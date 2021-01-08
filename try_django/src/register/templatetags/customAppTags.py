from django import template
import random
from django.conf import settings
register = template.Library()

def sendOTP(recipient):
    otp = random.randint(9999,100000)
    subject = "Rebuild your password using this OTP {0}".format(otp)
    message = "don't share this email"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [recipient,]
    send_mail(subject,message,email_from,recipient_list)
