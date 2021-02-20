from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group


from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from doctor.models import DoctorInfo
from patient.models import Profile,Feedback,Disease1,WhoPredictDisease
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.db.models import Q
from doctor.forms import DoctorForm,DoctorUserForm

from roleadmin.forms import AddDiseaseForm
# Create your views here.
@login_required(login_url="roleadmin_login")
def admin_dashboard(request):
    doctors=DoctorInfo.objects.all().count()
    users=User.objects.filter(groups__name="PATIENT").count()
    # patients=Profile.objects.all().count()
    feedbacks=Feedback.objects.all().count()
    doctorinfo=DoctorInfo.objects.all().order_by('-id')
    predictions=WhoPredictDisease.objects.all().count()
    patient_list=WhoPredictDisease.objects.all().order_by('-id')
    context={
        'doctors':doctors,
        'patients':users,
        'feedbacks':feedbacks,
        'doctorinfo':doctorinfo,
        'predictions':predictions,
        'patient_list':patient_list,
    }
    return render(request,'roleadmin/dashboard.html',context)

@login_required(login_url="roleadmin_login")
def disease(request):
    # page=request.GET.get('page',1)
    search_term=request.GET.get('term')
    if search_term==None:
        search_term=""
    diseases=Disease1.objects.filter(Q(name__icontains=search_term)|Q(doctor__user__first_name__icontains=search_term)|Q(doctor__user__last_name__icontains=search_term)).order_by('-id')
    # doctors=DoctorInfo.objects.filter(Q(name__icontains=search_term) | Q(address__icontains=search_term)| Q(department__icontains=search_term))
    # doctors=DoctorInfo.objects.filter(Q(user__first_name__icontains=search_term) |Q(user__last_name__icontains=search_term)|Q(address__icontains=search_term)| Q(department__icontains=search_term))
    # doctors=DoctorInfo.objects.all()
    # paginator=Paginator(diseases,8)
    # try:
        # diseases=paginator.page(page)
    # except PageNotAnInteger:
        # diseases=paginator.page(1)
    # except EmptyPage:
        # diseases=paginator.page(paginator.num_pages)
    context={
        'diseases':diseases,
    } 
    # return render(request,'roleadmin/doctor_list.html',context)   
    return render(request,'roleadmin/disease.html',context)

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
def edit_disease(request,pk):
    try:
        disease=Disease1.objects.get(id=pk)
    except:
        return redirect('disease')        
    assign_disease_form=AddDiseaseForm(request.POST,instance=disease)
    mydict={'assign_disease_form':assign_disease_form,'disease':disease}
    if request.method=='POST':
        assign_disease_form=AddDiseaseForm(request.POST,instance=disease)
        if assign_disease_form.is_valid():
            assign_disease_form.save()
            return redirect('disease')
    return render(request,'roleadmin/assign_disease_edit_form.html',context=mydict)

@login_required(login_url="roleadmin_login")
def delete_disease(request,pk):
    try:
        disease=Disease1.objects.get(id=pk)
    except:
        return redirect('disease')
    disease.delete()
    return redirect('disease')
    # disease=Disease1.objects.filter()
@login_required(login_url="roleadmin_login")
def doctors_list(request):
    page=request.GET.get('page',1)
    search_term=request.GET.get('term')
    if search_term==None:
        search_term=""
    # doctors=DoctorInfo.objects.filter(Q(name__icontains=search_term) | Q(address__icontains=search_term)| Q(department__icontains=search_term))
    doctors=DoctorInfo.objects.filter(Q(user__first_name__icontains=search_term) |Q(user__last_name__icontains=search_term)|Q(address__icontains=search_term)| Q(department__icontains=search_term))
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

# @login_required(login_url="roleadmin_login")
# def add_doctor(request):
#     if request.method=='POST':
#         doctor_add_form=DoctorForm(request.POST or None,request.FILES or None)
#         if doctor_add_form.is_valid():
#             add_doctor=doctor_add_form.save(commit=False)
#             # add_feedback.uploaded_by=request.user.profile
#             add_doctor.save()
#             return redirect('doctors_list')
#         else:
#             context={
#                 'doctor_add_form':doctor_add_form
#             }
#             return render(request,'roleadmin/doctor_add_form.html',context)
#     else:
#         doctor_add_form=DoctorForm()
#         context={
#             'doctor_add_form':doctor_add_form
#         }
#         return render(request,'roleadmin/doctor_add_form.html',context)
@login_required(login_url="roleadmin_login")
def add_doctor(request):
    userForm=DoctorUserForm()
    doctor_add_form=DoctorForm()
    mydict={'userForm':userForm,'doctor_add_form':doctor_add_form}
    if request.method=='POST':
        userForm=DoctorUserForm(request.POST)
        doctor_add_form=DoctorForm(request.POST,request.FILES)
        if userForm.is_valid() and doctor_add_form.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            doctor=doctor_add_form.save(commit=False)
            doctor.user=user
            doctor.save()
            my_doctor_group=Group.objects.get_or_create(name='DOCTOR')
            my_doctor_group[0].user_set.add(user)
        return redirect('doctors_list')
    return render(request,'roleadmin/doctor_add_form.html',context=mydict)



@login_required(login_url='roleadminlogin')
def edit_doctor(request,pk):
    try:
        doctor=DoctorInfo.objects.get(id=pk)
    except:
        return redirect('doctors_list')        
    user=User.objects.get(id=doctor.user_id)
    userForm=DoctorUserForm(instance=user)
    doctor_add_form=DoctorForm(request.FILES,instance=doctor)
    mydict={'userForm':userForm,'doctor_add_form':doctor_add_form,'doctor':doctor}
    if request.method=='POST':
        userForm=DoctorUserForm(request.POST,instance=user)
        doctor_add_form=DoctorForm(request.POST,request.FILES,instance=doctor)
        if userForm.is_valid() and doctor_add_form.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            doctor_add_form.save()
            return redirect('doctors_list')
    return render(request,'roleadmin/doctor_edit_form.html',context=mydict)

@login_required(login_url="roleadmin_login")
def delete_doctor(request,pk):
    try:
        doctor=DoctorInfo.objects.get(id=pk)
    except:
        return redirect('doctors_list')        
    user=User.objects.get(id=doctor.user_id)
    user.delete()
    doctor.delete()
    return redirect('doctors_list')

@login_required(login_url="roleadmin_login")
def patients_list(request):
    search_term=request.GET.get('term')
    users=User.objects.filter(groups__name="PATIENT")
    if search_term==None:
        search_term=""
    patients=Profile.objects.filter(user_id__in=users).filter(Q(name__icontains=search_term) | Q(user__email__icontains=search_term) | Q(address__icontains=search_term))
    context={
        'patients':patients,
    }
    return render(request,'roleadmin/patient_list.html',context)

@login_required(login_url="roleadmin_login")
def patient_profile(request,pk):
    try:
        users=User.objects.filter(groups__name="PATIENT")
        patient=Profile.objects.filter(user_id__in=users).get(id=pk)
        print(patient)
    except:
        return redirect('patients_list')
    context={
        'patient':patient
    }
    return render(request,'roleadmin/patient_profile.html',context)

@login_required(login_url="roleadmin_login")
def patient_delete(request,pk):
    try:
        users=User.objects.filter(groups__name="PATIENT")
        patient=Profile.objects.filter(user_id__in=users).get(id=pk)
    except:
        return redirect('patients_list')        
    # user=User.objects.get(id=doctor.user_id)
    # user.delete()
    patient.delete()
    return redirect('patients_list')    

@login_required(login_url='roleadmin_login')
def our_feedback(request):
    page=request.GET.get('page',1)
    feedbacks=Feedback.objects.all().order_by('-id')
    paginator=Paginator(feedbacks,9)
    try:
        feedbacks=paginator.page(page)
    except PageNotAnInteger:
        feedbacks=paginator.page(1)
    except EmptyPage:
        feedbacks=paginator.page(paginator.num_pages)
    context={
        'feedbacks':feedbacks
    }
    return render(request,'roleadmin/feedback.html',context)

@login_required(login_url='roleadmin_login')
def our_feedback_detail(request,pk):
    try:
        feedback=Feedback.objects.get(id=pk)
    except:
        return redirect('our_feedback')
    print(feedback)
    context={
        "feedback":feedback
    }
    return render(request,'roleadmin/feedback_detail.html',context)

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





