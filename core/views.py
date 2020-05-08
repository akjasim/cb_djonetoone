from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from core.models import Phone


def my_view(request):
    user_phone = User.objects.get(id=1).no
    print(type(user_phone))

    user = Phone.objects.get(id=1).user_id
    print(type(user))

