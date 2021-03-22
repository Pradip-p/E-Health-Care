from django.shortcuts import render, redirect
from patient.forms import *
from django.contrib.auth import authenticate, logout,login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from patient.models import Profile
from django.db import transaction
from patient.models import *
# from patient.models import Diabetes
# Create your views here.

# decorators

from patient.patient_decorators import unauthenticated_patient,allowed_users

from django.shortcuts import render, HttpResponse
import requests

from Health.forms import *
from api.models import Disease
from api import diseaseml

from patient.heart import pred_heart
from patient.image_block import predImageBlock
from patient.Diabetes import pred_diabetes
from patient.pneumonia import pred1
from api.diseaseml import pred
from .models import Image
from django.contrib.auth.models import Group

from django.db.models import Q
# Pagination import 
# from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


#For Pnemonia check
@login_required(login_url='patient_login')
@allowed_users(allowed_roles=['PATIENT'])
def showimage(request): 
    form= BlockImageForm(request.POST, request.FILES)


    if form.is_valid():
        form.save()
        lastimage = ImageBlock.objects.latest('id')
        imagefile = lastimage.imageblock
        result = predImageBlock(imagefile)


        if result[0][0] >= 0.5:

            #For pnenumonia prediction

            result=pred1(imagefile)
        
            context={}
            if result[0][0] == 1:
                prediction = 'You are suffering from pneumonia'
                disease_name="Pneumonia"
                # saving  user information who predict pneumonia and suggesting doctors
                predict=WhoPredictDisease(predict_by=request.user.profile,predicted_disease=disease_name)
                predict.save()
                disease=Disease1.objects.filter(name__icontains=disease_name)
                listDoctorID=[]
                for d in disease:
                    listDoctorID.append(d.doctor.id)
                disease_doctor_list=DoctorInfo.objects.filter(Q(id__in=listDoctorID))
                context= {
                'imagefile':imagefile,
                'form': form,
                'sur':prediction,
                'disease_doctor_list':disease_doctor_list,
                }
                return render(request, 'patient/image.html', context)
            else:
                prediction = "Your health is Normal"
                context= {
                'imagefile':imagefile,
                'form': form,
                'sur':prediction,
                }        
                return render(request, 'patient/image.html', context)

        else:   
            prediction = "You can not upload this image"
            contex = {'sur': prediction}
            return render(request, 'patient/image.html', contex)
    if request.method == "GET":
        sur = ' '
        imagefile = ''
        context= {
            'imagefile':imagefile,
            'form': form,
            'sur':sur,
            }
        return render(request, 'patient/image.html', context)
    


    # if form.is_valid():
    #     form.save()
    #     lastimage= Image.objects.last()
    #     imagefile= lastimage.imagefile
        
        # result=pred1(imagefile)
        
        # context={}
        # if result[0][0] >= 0.5:
        #     prediction = 'You are suffering from pneumonia'
        #     disease_name="Pneumonia"
        #     # saving  user information who predict pneumonia and suggesting doctors
        #     predict=WhoPredictDisease(predict_by=request.user.profile,predicted_disease=disease_name)
        #     predict.save()
        #     disease=Disease1.objects.filter(name__icontains=disease_name)
        #     listDoctorID=[]
        #     for d in disease:
        #         listDoctorID.append(d.doctor.id)
        #     disease_doctor_list=DoctorInfo.objects.filter(Q(id__in=listDoctorID))
        #     context= {
        #     'imagefile':imagefile,
        #     'form': form,
        #     'sur':prediction,
        #     'disease_doctor_list':disease_doctor_list,
        #     }
        #     return render(request, 'patient/image.html', context)
        # elif result[0][0] <= 0.5:
        #     prediction = "Your health is Normal"
        #     context= {
        #     'imagefile':imagefile,
        #     'form': form,
        #     'sur':prediction,
        #     }        
        #     return render(request, 'patient/image.html', context)
    


    
@login_required(login_url='patient_login')
@allowed_users(allowed_roles=['PATIENT'])
def diabetes(request):

    if request.method == "GET":
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
            ob = Diabetes.objects.latest('id')

            sur=pred_diabetes(ob)
            
            # print('*'*8,sur)

            sur=", ".join( repr(e) for e in sur).strip("''")
            # print("***********", sur)
            
            if sur== '1':
                context = {}
                result= "Yes, You are suffering  from Diabetes problems"
                predicted_disease_name="Diabetes"
                predict=WhoPredictDisease(predict_by=request.user.profile,predicted_disease=predicted_disease_name)
                predict.save()
                disease=Disease1.objects.filter(name__icontains=predicted_disease_name)
                listDoctorID=[]
                for d in disease:
                    listDoctorID.append(d.doctor.id)
                disease_doctor_list=DoctorInfo.objects.filter(Q(id__in=listDoctorID))
                
                context={
                    'sur': result,
                    'disease_doctor_list':disease_doctor_list,
                }
                return render(request,'patient/diabetes_results.html', context)

            elif sur=='0':
                context = {}
                context={'sur':'You are not suffering from diabetes problem',}
                return render(request,'patient/diabetes_results.html', context)



@login_required(login_url='patient_login')
@allowed_users(allowed_roles=['PATIENT'])
def heart(request):
    if request.method=="GET":
        heart_form=HeartForm()
        contex={
            'heart_form':heart_form
        }
        return render(request,'patient/heart.html', contex)
    if request.method =="POST":
        contex = {}
        if request.POST.get('age'):
            heart = Heart()

            age = request.POST.get('age')
        
            
            sex = request.POST.get('sex')
            sex = sex.lower()
            if sex == 'male':
                sex = 1
            elif sex == 'female':
                sex = 0
            elif sex == 'other':
                sex = 0.5
            
            cp = request.POST.get('cp')
            cp = cp.lower()
            if cp == "typical angina":
                cp = 0
            elif cp == "atypical angina":
                cp = 1
            elif cp == "non-anginal pain":
                cp = 2
            elif cp == 'asymptomatic':
                cp == 3

            
            trestbps = request.POST.get('trestbps')
            
            chol = request.POST.get('chol')
            
            fbs = request.POST.get('fbs')
            fbs = fbs.lower()
            if fbs == 'true':
                fbs = 1
            elif fbs == 'false':
                fbs = 0

            restecg = request.POST.get('restecg')
            restecg = restecg.lower()
            if restecg == "normal":
                restecg = 0
            elif restecg == "having st-t":
                restecg = 1
            elif restecg == 'hypertrophy':
                restecg = 2

            thalach = request.POST.get('thalach')
        

            exang = request.POST.get('exang')
            exang = exang.lower()

            if exang== 'yes':
                exang = 1
            elif exang == 'no':
                exang = 0
            oldpeak = request.POST.get('oldpeak')
            slope = request.POST.get('slope')
            slope = slope.lower()
            if slope =='upsloping':
                slope = 0
            elif slope == 'flat':
                slope = 1
            elif slope=='downsloping':
                slope =2

            ca = request.POST.get('ca')

            thal = request.POST.get('thal')
            thal = thal.lower()

            if thal =="normal":
                thal = 0
            elif thal == 'fixed defect':
                thal = 1
            elif thal =="reversable defect":
                thal = 2


            heart.age = age
            heart.sex = sex
            heart.cp = cp
            heart.chol = chol
            heart.trestbps = trestbps
            heart.fbs = fbs
            heart.restecg = restecg
            heart.thalach = thalach
            heart.exang = exang
            heart.oldpeak = oldpeak
            heart.slope = slope
            heart.ca = ca
            heart.thal = thal
            print(age,sex,cp,chol,trestbps,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
            heart.save()

            ob=Heart.objects.latest('id')
            sur=pred_heart(ob)
            sur=", ".join( repr(e) for e in sur).strip("''")
            context={}
            if sur== '1':
                
                name= "Yes, You are suffuring from heart problems"
                predicted_disease_name="Heart"
                predict=WhoPredictDisease(predict_by=request.user.profile,predicted_disease=predicted_disease_name)
                predict.save()
                disease=Disease1.objects.filter(name__icontains=predicted_disease_name)
                listDoctorID=[]
                for d in disease:
                    listDoctorID.append(d.doctor.id)
                disease_doctor_list=DoctorInfo.objects.filter(Q(id__in=listDoctorID))
                context={
                    'sur':name,
                    'disease_doctor_list':disease_doctor_list
                }
            elif sur=='0':
                name="You are not suffuring from heart problems"
                context={
                    'sur':name,
                }
            
            return render(request,'patient/heart_results.html', context)
            

@login_required(login_url='patient_login')
@allowed_users(allowed_roles=['PATIENT'])
def dashboard(request):
    if request.method =="POST":
        contex = {}
        if request.POST.get('value1'):
            disease = Disease()
            value1 = request.POST.get('value1')
            
            value2 = request.POST.get('value2')
            
            value3 = request.POST.get('value3')
            
            value4 = request.POST.get('value4')
            
            value5 = request.POST.get('value5')
            
            value6 = request.POST.get('value6')

            disease.value_1 = value1
            disease.value_2 = value2
            disease.value_3 = value3
            disease.value_4 = value4
            disease.value_5 = value5
            disease.value_6 = value6
            disease.save()
            ob = Disease.objects.latest('id')
            sur = pred(ob)
            predicted_disease_name = sur[0][0]
            symptoms = sur[1]
        
            value1 = symptoms[0]
            value2 = symptoms[1]
            value3 = symptoms[2]
            value4 = symptoms[3]
            value5 = symptoms[4]
            value6 = symptoms[5]
            
            # patient who predrict disease is save in now database
            predict=WhoPredictDisease(predict_by=request.user.profile,predicted_disease=predicted_disease_name)
            predict.save()
            disease=Disease1.objects.filter(name__icontains=predicted_disease_name)
            listDoctorID=[]
            for d in disease:
                listDoctorID.append(d.doctor.id)
            disease_doctor_list=DoctorInfo.objects.filter(Q(id__in=listDoctorID))
                        
           

        return render(request, 'patient/showDisease.html', context = {"Predicted_disease":predicted_disease_name,'disease_doctor_list':disease_doctor_list,"value1": value1, 		"value2":value2, "value3":value3, "value4": value4, "value5":value5, "value6": value6})

    else:
        return render(request, 'patient/dashboard.html')
    

@login_required(login_url='patient_login')



@login_required(login_url='patient_login')
@allowed_users(allowed_roles=['PATIENT'])
def feedback(request):
    page=request.GET.get('page',1)
    feedbacks=Feedback.objects.filter(Q(uploaded_by=request.user.profile)).order_by('-id')
    paginator=Paginator(feedbacks,8)
    try:
        feedbacks=paginator.page(page)
    except PageNotAnInteger:
        feedbacks=paginator.page(1)
    except EmptyPage:
        feedbacks=paginator.page(paginator.num_pages)
    context={
        'feedbacks':feedbacks
    }
    return render(request,'patient/feedback.html',context)

@login_required(login_url='patient_login')
@allowed_users(allowed_roles=['PATIENT'])
def feedback_detail(request,pk):
    feedback=Feedback.objects.get(id=pk,uploaded_by=request.user.profile)
    print(feedback)
    context={
        "feedback":feedback
    }
    return render(request,'patient/feedback_detail.html',context)

@login_required(login_url='patient_login')
@allowed_users(allowed_roles=['PATIENT'])
def feedback_delete(request,pk):
    try:
        feedback=Feedback.objects.get(id=pk,uploaded_by=request.user.profile)
    except:
        return redirect('feedback')
    feedback.delete()
    return redirect('feedback')

@login_required(login_url='patient_login')
@allowed_users(allowed_roles=['PATIENT'])
def feedback_edit(request,pk):
    try:
        feedback=Feedback.objects.get(id=pk,uploaded_by=request.user.profile)
    except:
        return redirect('feedback')
    if request.method=='POST':   
        feedback_edit_form=FeedbackForm(request.POST or None,request.FILES,instance=feedback)
        if feedback_edit_form.is_valid():
            update=feedback_edit_form.save(commit=False)
            update.uploaded_by=request.user.profile
            update.save()
            return redirect('feedback')
        else:
            context={
                'feedback_edit_form':feedback_edit_form,
                'feedback':feedback
            }
            return render(request,'patient/feedback_edit_form.html',context)
    else:
        feedback_form=FeedbackForm(request.POST or None,request.FILES,instance=feedback)
        context={
            'feedback_form':feedback_form,
            'feedback':feedback
        }
        return render(request,'patient/feedback_edit_form.html',context)

@login_required(login_url='patient_login')
@allowed_users(allowed_roles=['PATIENT'])
def feedback_add(request):
    if request.method=='POST':
        feedback_add_form=FeedbackForm(request.POST or None,request.FILES or None)
        if feedback_add_form.is_valid():
            add_feedback=feedback_add_form.save(commit=False)
            add_feedback.uploaded_by=request.user.profile
            add_feedback.save()
            return redirect('feedback')
        else:
            context={
                'feedback_add_form':feedback_add_form
            }
            return render(request,'patient/feedback_add_form.html',context)
    else:
        feedback_add_form=FeedbackForm()
        context={
            'feedback_add_form':feedback_add_form
        }
        return render(request,'patient/feedback_add_form.html',context)

@login_required(login_url='patient_login')
@allowed_users(allowed_roles=['PATIENT'])
def search_doctor(request):
    context={}
    if request.method=="POST":
        search_term=request.POST.get('term')
        disease=Disease1.objects.filter(name__icontains=search_term)
        if search_term==None:
            search_term=""
        doctorID=[]
        for d in disease:
            doctorID.append(d.doctor.id)
        doctors=DoctorInfo.objects.filter(id__in=doctorID) or DoctorInfo.objects.filter(Q(user__first_name__icontains=search_term)|Q(user__last_name__icontains=search_term)|Q(department__icontains=search_term))
        context={
            'doctors':doctors,
        }
        return render(request,'patient/search_doctor.html',context)
    else:
        doctors=[]
        context={
            "doctors":doctors,
        }
        return render(request,'patient/search_doctor.html',context)

@login_required(login_url='patient_login')
@allowed_users(allowed_roles=['PATIENT'])
def doctor_profile(request,pk):
    doctor=DoctorInfo.objects.get(id=pk)
    # print(doctor.__dict__)
    context={
        'doctor':doctor,
    }
    return render(request,'patient/doctor_profile.html',context)


@login_required(login_url='patient_login')
@allowed_users(allowed_roles=['PATIENT'])
def my_profile(request):
    return render(request,'patient/my_profile.html')



@login_required(login_url='patient_login')
@allowed_users(allowed_roles=['PATIENT'])
def home(request):
    page=request.GET.get('page',1)
    search_term=request.GET.get('term')
    if search_term==None:
        search_term=""
    doctors=DoctorInfo.objects.filter(Q(user__first_name__icontains=search_term) |Q(user__last_name__icontains=search_term)|Q(address__icontains=search_term)| Q(department__icontains=search_term))
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



@unauthenticated_patient
def patient_register(request):
    patient_register=UserForm()
    if request.method == 'POST':
        patient_register= UserForm(request.POST)
        if patient_register.is_valid():
            user=patient_register.save()
            my_patient_group=Group.objects.get_or_create(name="PATIENT")
            my_patient_group[0].user_set.add(user)
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
@allowed_users(allowed_roles=['PATIENT'])
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

@unauthenticated_patient
def patient_login(request):
    if request.method=="POST":
        username = request.POST.get('username')       
        password = request.POST.get('password') 
        user =authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request, "Please enter valid credentials")
            # messages.info(request, "Invalid username or password")
            return render(request, 'patient/login.html')
    else:
        return render(request, 'patient/login.html')

def logoutpatient(request):
    print("logout user")
    logout(request)
    return redirect("/")
