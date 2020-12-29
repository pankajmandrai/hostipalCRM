from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import logout

# Create your views here.
from .models import DoctorMore, Doctor, Clients, PatientMore, Patient, Staff, StaffMore


def index(request):
    # return HttpResponse("<h1>Home page{form}</h1>",)
    return render(request, 'home.html')


def login(request):
    try:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            print(username, password)
            client = Clients.objects.get(email=username)
            if client.password == password:
                # password was correct
                if client.type == "DOCTOR":
                    return render(request, 'dashboard.html', {'name': client.username})
                elif client.type == "PATIENT":
                    return render(request, 'dashboard.html', {'name': client.username})
                elif client.type == "STAFF":
                    return render(request, 'dashboard.html', {'name': client.username})
                else:
                    return HttpResponse("yourn't belong here, check your type")
            return HttpResponse("pasword is not match or email doesn't exist")
        else:
            return render(request, "login.html")
            # return HttpResponse("<button> </button>")
    except Exception as e:
        return HttpResponse(e)


def signup(request, name):
    password_check = False
    try:
        if request.method == 'POST':
            email = request.POST['email']
            username = request.POST['username']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            if password1 == password2:
                password_check = True
            if name == "DOCTOR":
                department = request.POST['department']
                print(username, password1, password2, email, department)
                if password_check:
                    doct_obj = Doctor.objects.create(
                        username=username, email=email, password=password1)
                    Doctor.save
                    DoctorMore.objects.create(
                        user=doct_obj, department=department)
                    DoctorMore.save
                    return redirect('/login/')
                else:
                    return HttpResponse("retype password correctly")
            elif name == "PATIENT":
                disease = request.POST['disease']
                if password_check:
                    pat_obj = Patient.objects.create(
                        username=username, email=email, password=password1)
                    PatientMore.objects.create(user=pat_obj, disease=disease)
                    return redirect('/login/')
                else:
                    return HttpResponse("retype password correctly")
            elif name == "STAFF":
                shift = request.POST['shift']
                if password_check:
                    sta_obj = Staff.objects.create(
                        username=username, email=email, password=password1)
                    StaffMore.objects.create(user=sta_obj, shift=shift)
                    return redirect('/login/')
                else:
                    return HttpResponse("retype password correctly")

        else:
            print(name)
            return render(request, 'signup.html', {'name': name})
    except Exception as _:
        print(_)
        return HttpResponse("<h1>we faced a issue, we will be back with solution</h1>")
