from django.shortcuts import render, redirect
from patient.forms import PatientInfoForm, UserForm
from django.contrib.auth import authenticate, logout,login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserCreationForm

# Create your views here.
@login_required(login_url='patient_login')
def dashboard(request):
    contex={}
    return render(request, 'patient/dashboard.html', contex)


def patient_register(request):
    patient_register=UserForm()
    if request.method == 'POST':
        patient_register= UserForm(request.POST)
        if patient_register.is_valid():
            patient_register.save()
            # register.set_password(register.password)
            return redirect("patient_login")
        else:
            contex={
                'patient_register':patient_register
            }
            print("in valid inputs")
            return render(request, 'patient/register.html', contex)
    else:     
        patient_register=UserForm()
        # patient_register=PatientRegisterForm()
        contex={
            'patient_register':patient_register,
        }
        return render(request, 'patient/register.html', contex)
    



def patient_login(request):
    if request.method=="POST":
        username = request.POST.get('username')       
        password = request.POST.get('password') 
        user =authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            # return render(request, 'patient/dashboard.html')
            return redirect('dashboard')
        else:
            messages.info(request, "Invalid Username or password")
            return render(request, 'patient/login.html')
    else:
        return render(request, 'patient/login.html')
def logoutpatient(request):
    print("logout user")
    logout(request)
    return redirect("/")