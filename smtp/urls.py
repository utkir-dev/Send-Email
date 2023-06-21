from django.urls import path

from smtp.views import home,send_email

urlpatterns = [
    path('', home,name='home'),
    path('send/', send_email,name='send_email'),
]
