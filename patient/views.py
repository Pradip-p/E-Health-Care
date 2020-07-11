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
from Health.forms import DiseaseForm, HeartForm, DiabetesForm
from api.models import Disease
from api import diseaseml
# from . import heart
from patient.heart import pred
from patient.Diabetes import pred



# @login_required(login_url='patient_login')
# def dashboard(request):
#     contex={}
#     return render(request, 'patient/dashboard.html', contex)


@login_required(login_url='patient_login')
def Diabetes(request):
    if request.method=="GET":
        diabetes_form=DiabetesForm()
        contex={
            'diabetes_form':diabetes_form
        }
        return render(request,'patient/diabetes.html', contex)
    elif  request.method=="POST":
        diabetes_form=DiabetesForm(request.POST)
        if diabetes_form.is_valid:
            diabetes_form.save()
            from patient.models import Diabetes
            ob=Diabetes.objects.latest('id')
            print(ob)
            sur=pred(ob)
            sur=", ".join( repr(e) for e in sur).strip("''")
            if sur== '1':
                name= "Yes, You are suffering  from Diabetes problems"
            elif sur=='0':
                name="You are not suffering from Diabetes prolems"
                
            contex={
                'sur':name,
            }

            return render(request,'patient/diabetes_results.html', contex)


@login_required(login_url='patient_login')
def heart(request):
    if request.method=="GET":
        heart_form=HeartForm()
        contex={
            'heart_form':heart_form
        }
        return render(request,'patient/heart.html', contex)
    elif  request.method=="POST":
        heart_form=HeartForm(request.POST)
        if heart_form.is_valid:
            heart_form.save()
            ob=Heart.objects.latest('id')
            print(ob)
            sur=pred(ob)
            sur=", ".join( repr(e) for e in sur).strip("''")
            if sur== '1':
                name= "Yes, You are suffuring from heart problems"
            elif sur=='0':
                name="You are not suffuring from heart problmes"
                
            contex={
                'sur':name,
            }
            return render(request,'patient/heart_results.html', contex)



@login_required(login_url='patient_login')
def search_doctor(request):
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
            return render(request,'patient/search_doctor.html', contex)


        
    else:
        contex={}
        return render(request,'patient/search_doctor.html', contex)




# @login_required(login_url='patient_login')
# def dashboard(request):
#     if request.method=="POST":
#         disease_form=DiseaseForm(request.POST)
#         if disease_form.is_valid:
#             disease_form.save()
#             ob=Disease.objects.latest('id')
#             sur=diseaseml.pred(ob)
#             print("@"*80)
#             print(sur)
#             contex={"Disease":sur}
#             # ob=Doctor.objects.get(pk=1)
#             # if sur==ob:
        
#             return render(request,'patient/dashboard.html', contex)
#     else:
#         disease_form=DiseaseForm()
#         contex={
#             'disease_form':disease_form
#         }
#         return render(request, 'patient/dashboard.html', contex)


@login_required(login_url='patient_login')
def my_profile(request):
    return render(request,'patient/my_profile.html')


@login_required(login_url='patient_login')
def dashboard(request):
    if request.method=="POST":
        disease_form=DiseaseForm(request.POST)
        if disease_form.is_valid:
            disease_form.save()
            ob=Disease.objects.latest('id')
            sur=diseaseml.pred(ob)
            
            print("@"*80)
            sur=", ".join( repr(e) for e in sur).strip("''")
            disease=Disease1.objects.all()
            for i in disease:
                print(i)
                if sur==i.name:
                    ob=Disease1.objects.get(name=sur)
                    doctor_name=ob.category.name
                    phone=ob.category.phone_number
                    email=ob.category.email
                    print("Yes, finally working !!")

            # if sur==i

            contex={"Disease":sur,
            'name':doctor_name,
            'phone':phone,
            'email':email}
            return render(request,'patient/show_doctor_info.html', contex)
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
            return redirect("my_profile")
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