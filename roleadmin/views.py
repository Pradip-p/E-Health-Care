from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from doctor.models import DoctorInfo
from patient.models import Profile,Feedback
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.db.models import Q
from doctor.forms import DoctorForm

from roleadmin.forms import AddDiseaseForm
# Create your views here.
@login_required(login_url="roleadmin_login")
def admin_dashboard(request):
    doctors=DoctorInfo.objects.all().count()
    patients=Profile.objects.all().count()
    feedbacks=Feedback.objects.all().count()
    doctorinfo=DoctorInfo.objects.all().order_by('-id')
    context={
        'doctors':doctors,
        'patients':patients,
        'feedbacks':feedbacks,
        'doctorinfo':doctorinfo,
    }
    return render(request,'roleadmin/dashboard.html',context)

@login_required(login_url="roleadmin_login")
def disease(request):
   
    return render(request,'roleadmin/disease.html')

@login_required(login_url="roleadmin_login")
def assign_disease(request):
    if request.method=="POST":
        assign_disease_form=AddDiseaseForm(request.POST or None)
        if assign_disease_form.is_valid():
            assign_disease_form.save()
            return redirect('disease')
        else:
            context={
                'assign_disease_form':assign_disease_form
            }
            return render(request,'roleadmin/assign_disease_form.html',context)
    else:
        assign_disease_form=AddDiseaseForm()  
        context={
            'assign_disease_form':assign_disease_form
        }
        return render(request,'roleadmin/assign_disease_form.html',context)

@login_required(login_url="roleadmin_login")
def doctors_list(request):
    page=request.GET.get('page',1)
    search_term=request.GET.get('term')
    if search_term==None:
        search_term=""
    doctors=DoctorInfo.objects.filter(Q(name__icontains=search_term) | Q(address__icontains=search_term)| Q(department__icontains=search_term))
    # doctors=DoctorInfo.objects.all()
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
    return render(request,'roleadmin/doctor_list.html',context)

@login_required(login_url="roleadmin_login")
def add_doctor(request):
    if request.method=='POST':
        doctor_add_form=DoctorForm(request.POST or None,request.FILES or None)
        if doctor_add_form.is_valid():
            add_doctor=doctor_add_form.save(commit=False)
            # add_feedback.uploaded_by=request.user.profile
            add_doctor.save()
            return redirect('doctors_list')
        else:
            context={
                'doctor_add_form':doctor_add_form
            }
            return render(request,'roleadmin/doctor_add_form.html',context)
    else:
        doctor_add_form=DoctorForm()
        context={
            'doctor_add_form':doctor_add_form
        }
        return render(request,'roleadmin/doctor_add_form.html',context)

@login_required(login_url="roleadmin_login")
def edit_doctor(request,pk):
    try:
        doctor=DoctorInfo.objects.get(id=pk)
    except:
        return redirect('doctors_list')
    if request.method=='POST':   
        doctor_edit_form=DoctorForm(request.POST or None,request.FILES,instance=doctor)
        if doctor_edit_form.is_valid():
            update=doctor_edit_form.save(commit=False)
            # update.uploaded_by=request.user.profile
            update.save()
            return redirect('doctors_list')
        else:
            print(doctor_edit_form.errors)
            context={
                'doctor_edit_form':doctor_edit_form,
                'doctor':doctor
            }
            return render(request,'roleadmin/doctor_edit_form.html',context)
    else:
        doctor_edit_form=DoctorForm()
        context={
            'doctor_edit_form':doctor_edit_form,
            'doctor':doctor
        }
        return render(request,'roleadmin/doctor_edit_form.html',context)

@login_required(login_url="roleadmin_login")
def delete_doctor(request,pk):
    try:
        doctor=DoctorInfo.objects.get(id=pk)
    except:
        return redirect('doctors_list')
    doctor.delete()
    return redirect('doctors_list')

@login_required(login_url="roleadmin_login")
def patients_list(request):
    search_term=request.GET.get('term')
    if search_term==None:
        search_term=""
    patients=Profile.objects.filter(Q(name__icontains=search_term) | Q(user__email__icontains=search_term) | Q(address__icontains=search_term))
    context={
        'patients':patients,
    }
    return render(request,'roleadmin/patient_list.html',context)
def roleadmin_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        superuser=User.objects.filter(username=username,is_superuser=True)
        if superuser:
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('admin_dashboard')
            else:
                messages.info(request,'Please enter valid credentials')
                return render(request,'roleadmin/login.html')
        else:
            messages.info(request,'You are not authorized user')
            return render(request,'roleadmin/login.html')
    else:
        return render(request,'roleadmin/login.html')

def roleadmin_logout(request):
    logout(request)
    return redirect("/")





