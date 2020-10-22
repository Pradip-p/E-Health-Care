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

from django.shortcuts import render, HttpResponse
import requests

from Health.forms import *
from api.models import Disease
from api import diseaseml
# from . import heart
from patient.heart import pred_heart
from patient.Diabetes import pred
from patient.pneumonia import pred1
from .models import Image

from django.db.models import Q
# Pagination import 
# from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required(login_url='patient_login')
def showimage(request):   
    lastimage= Image.objects.last()
    imagefile= lastimage.imagefile
    form= ImageForm(request.POST or None, request.FILES or None)
    contex={'form': form}
    if form.is_valid():
        form.save()
        lastimage= Image.objects.last()
        imagefile= lastimage.imagefile
        print(imagefile)
        sur=pred1(imagefile)
        context= {
            'imagefile':imagefile,
            'form': form,
            'sur':sur,
            }
        return render(request, 'patient/image.html', context)
    sur = ' '
    context= {
        'imagefile':imagefile,
        'form': form,
        'sur':sur,
        }
    return render(request, 'patient/image.html', context)
    
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
            sur=pred_heart(ob)
            sur=", ".join( repr(e) for e in sur).strip("''")

            if sur== '1':
                name= "Yes, You are suffuring from heart problem"
            elif sur=='0':
                name="You are not suffuring from heart problme"
                
            contex={
                'sur':name,
            }
            return render(request,'patient/heart_results.html', contex)



@login_required(login_url='patient_login')

def form(request):
    pass
def search_doctor(request):
    context={}
    if request.method=="POST":
        search_term=request.POST.get('term')
        disease=Disease1.objects.filter(name__icontains=search_term)
        if search_term==None:
            search_term=""
        doctor_name=[]
        for d in disease:
            doctor_name.append(d.doctor)
        # page=request.GET.get('page',1) 
        doctors=DoctorInfo.objects.filter(Q(name__in=doctor_name) | Q(name__icontains=search_term))
        # count=doctors.count()
        # paginator=Paginator(doctors,3)
        # try:
        #     doctors=paginator.page(page)
        # except PageNotAnInteger:
        #     doctors=paginator.page(1)
        # except EmptyPage:
        #     doctors=paginator.page(paginator.num_pages) 
        # print(doctors)
        context={
            'doctors':doctors,
            # 'count':count
        }
        return render(request,'patient/search_doctor.html',context)

    # else:
    else:
        # page=request.GET.get('page',1)
        doctors=DoctorInfo.objects.all().order_by('-id')[:10]
        # count=doctors.count()
        # paginator=Paginator(doctors,3)
        # try:
        #     doctors=paginator.page(page)
        # except PageNotAnInteger:
        #     doctors=paginator.page(1)
        # except EmptyPage:
        #     doctors=paginator.page(paginator.num_pages) 
        context={
            "doctors":doctors,
            # "count":count
        }
        return render(request,'patient/search_doctor.html',context)

@login_required(login_url='patient_login')
def doctor_profile(request,pk):
    doctor=DoctorInfo.objects.get(id=pk)
    # print(doctor.__dict__)
    context={
        'doctor':doctor,
    }
    return render(request,'patient/doctor_profile.html',context)

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
            sur=", ".join( repr(e) for e in sur).strip("''")
            # disease_predicter=WhoPredictDisease()
            # disease_predicter.name=request.user.profile.name
            # disease_predicter.email=request.user.email
            # disease_predicter.phone_number=request.user.profile.phone_number
            # disease_predicter.predicted_disease=sur
            # disease_predicter.save()
            disease_doctor_list=Disease1.objects.filter(name=sur)
            contex={
            "Disease":sur,
            'disease_doctor_list':disease_doctor_list
            }
            return render(request,'patient/show_doctor_info.html', contex)
    else:
        print(request.user.username)

        disease_form=DiseaseForm()
        contex={
            'disease_form':disease_form
        }
        return render(request, 'patient/dashboard.html', contex)

@login_required(login_url='patient_login')
def home(request):
    page=request.GET.get('page',1)
    doctors=DoctorInfo.objects.all()
    paginator=Paginator(doctors,8)
    try:
        doctors=paginator.page(page)
    except PageNotAnInteger:
        doctors=paginator.page(1)
    except EmptyPage:
        doctors=paginator.page(paginator.num_pages)
    context={
        'doctors':doctors,
    } 
    return render(request,'patient/home.html',context)


def patient_register(request):
    patient_register=UserForm()
    if request.method == 'POST':
        patient_register= UserForm(request.POST)
        if patient_register.is_valid():
            patient_register.save()
            return redirect("patient_login")
        else:
            contex={
                'patient_register':patient_register
            }
            print("in valid inputs")
            return render(request, 'patient/register.html', contex)
    else:     
        patient_register=UserForm()
        contex={
            'patient_register':patient_register,
        }
        return render(request, 'patient/register.html', contex)





@login_required(login_url='patient_login') 
@transaction.atomic   
def patient_profile(request):
    if request.method=='POST':
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


def patient_login(request):
    if request.method=="POST":
        username = request.POST.get('username')       
        password = request.POST.get('password') 
        user =authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request, "Invalid Username or password")
            messages.info(request, "Invalid username or password")
            return render(request, 'patient/login.html')
    else:
        return render(request, 'patient/login.html')

def logoutpatient(request):
    print("logout user")
    logout(request)
    return redirect("/")