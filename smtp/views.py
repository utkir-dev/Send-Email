from django.http import HttpResponse
from django.shortcuts import render
from config import settings
#from email.message import EmailMessage

from django.core.mail import EmailMessage
# Create your views here.

def home(request):
    return render(request,"index.html")

def send_email(request):
    if request.method=='POST':
        name=request.POST['name']
        sender_email=request.POST['email']
        msg=request.POST['msg']
        phone=request.POST['phone']

        email=EmailMessage(
            f'Xabar qoldiruvchi: {sender_email}',
            f'Ismi: {name}\nXabari: {msg}\nTel raqami: {phone}',
            settings.EMAIL_HOST_USER,
            [sender_email]
        )
        email.fail_silently=True
        email.send()
        return HttpResponse("Muvaffaqiyatli jo'natildi")
    else:
        return HttpResponse("Jo'natilmadi")