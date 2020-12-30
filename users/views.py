from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages

from django.urls import reverse
# Create your views here.
from django.contrib.auth import authenticate, login


def login_request(request):
    if request.method == 'GET':
        return render(request, "users/login.html", {})
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if not (username and password):
            messages.add_message(request, messages.ERROR, "Enter username and password")
        user = authenticate(request, email=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('dashboard'))
        else:
            messages.add_message(request, messages.ERROR, "Enter correct username and password")
            return HttpResponseRedirect(reverse('login'))
    else:
        messages.add_message(request, messages.ERROR, "Invalid method")
        return redirect(reverse('login'))


def dashboard(request):
    return render(request, "users/dashboard.html", {})



#return redirect('dashboard/')
# return HttpResponseRedirect(reverse('dashboard'))