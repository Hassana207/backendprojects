from django.shortcuts import render,redirect
from .forms import RegisterUser
from django.contrib.auth import login

# Create your views here.

def register_user(request):
    if request.method == "POST":
        form = RegisterUser(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user )
            return redirect("homepage")
        else:
            form = RegisterUser()
    return render (request, "register.html",{"form":form})

