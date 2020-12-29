from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth import authenticate, login


def login_request(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('dashboard/')
    else:
        return redirect('login/')


def dashboard(request):
    return render(request, "dashboard.html", {})



#return redirect('dashboard/')
# return HttpResponseRedirect(reverse('dashboard'))