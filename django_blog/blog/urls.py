from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Django Blog!")

urlpatterns = [
    path('', home, name='home'),
]