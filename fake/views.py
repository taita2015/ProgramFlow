from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.http.response import HttpResponse
import random



def default_method(request):
    return HttpResponse("Tell me what you want to fake.<p>--Einstein</p>")



def fake_user(request):
    users = User.objects.all()
    u = random.choice(users)
    print(u)
    # u = User.objects.get(id=1)
    if u:
        login(request,u)

    #
    return render(request,'fake/fake_user.html',{"user":u})

    # return HttpResponseRedirect("/")
