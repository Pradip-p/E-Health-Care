from django.shortcuts import render, redirect
from patient.forms import *
from django.contrib.auth import authenticate, logout,login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from patient.models import Profile
from django.db import transaction
from patient.models import *
# Create your views here.

# Create your views here.
from django.shortcuts import render, HttpResponse
import requests
from Health.forms import DiseaseForm
from api.models import Disease
from api import diseaseml


# @login_required(login_url='patient_login')
# def dashboard(request):
#     contex={}
#     return render(request, 'patient/dashboard.html', contex)
@login_required(login_url='patient_login')
def form(request):
    contex={}
    if request.method=="POST":
        disease = request.POST.get('disease')   
        ob=Doctor.objects.get(pk=1)
        rog=ob.category.name
        print(rog)
        if rog==disease:
            name=ob.name
            contex={
                'name':name
            }
            return render(request,'patient/form.html', contex)


        
    else:
        contex={}
        return render(request,'patient/form.html', contex)




@login_required(login_url='patient_login')
def dashboard(request):
    if request.method=="POST":
        disease_form=DiseaseForm(request.POST)
        if disease_form.is_valid:
            disease_form.save()
            ob=Disease.objects.latest('id')
            sur=diseaseml.pred(ob)
            contex={"Disease":sur}
            return render(request,'patient/dashboard.html', contex)
    else:
        disease_form=DiseaseForm()
        contex={
            'disease_form':disease_form
        }
        return render(request, 'patient/dashboard.html', contex)


@login_required(login_url='patient_login')
def dashboard(request):
    if request.method=="POST":
        disease_form=DiseaseForm(request.POST)
        if disease_form.is_valid:
            disease_form.save()
            ob=Disease.objects.latest('id')
            sur=diseaseml.pred(ob)
            contex={"Disease":sur}
            return render(request,'patient/dashboard.html', contex)
    else:
        disease_form=DiseaseForm()
        contex={
            'disease_form':disease_form
        }
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


@login_required(login_url='patient_login') 
@transaction.atomic   
def patient_profile(request):
    if request.method=='POST':
        
        """patient=request.user
        print(patient)"""
        user_form=UpdateForm(request.POST,instance=request.user)
        patient_profile=ProfileForm(request.POST ,request.FILES ,instance=request.user.profile)
        if user_form.is_valid() and patient_profile.is_valid():
            user_form.save()
            patient_profile.save()
            return redirect("patient_profile")
        else:
            context={
                'user_form':user_form,
                'patient_profile':patient_profile
            }
            print('invalid inputs')
            return render(request,'patient/profile.html',context)

    else:
        user_form=UpdateForm(instance=request.user)
        patient_profile=ProfileForm(instance=request.user.profile)
        context={
            'user_form':user_form,
            'patient_profile':patient_profile,
        }
        return render(request,'patient/profile.html',context)
"""
@login_required
def patient_update(request):
    return render(request,'patient/update_profile.html')
"""


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