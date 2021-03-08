from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from doctor.models import DoctorInfo
from django.contrib import messages
from doctor.forms import UserForm
from django.db.models import Q

from django.contrib.auth.decorators import user_passes_test, login_required

from patient.models import Disease1, WhoPredictDisease
# Create your views here.
from doctor.doctor_decorators import unauthenticated_doctor,allowed_users
from django.contrib.auth.decorators import login_required


@unauthenticated_doctor
def doctor_login(request):
    if request.method=="POST":
        username = request.POST.get('username')       
        password = request.POST.get('password') 
        user =authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('dashboard_doctor')
        else:
            messages.info(request, "Please enter valid credentials")
            
            return render(request, 'doctor/login.html')
    else:
        return render(request, 'doctor/login.html')

   

def doctor_logout(request):
    print("logout user")
    logout(request)
    return redirect("/")

@login_required(login_url='doctor_login')
@allowed_users(allowed_roles=['DOCTOR'])
def dashboard_doctor(request):

    search_term = request.GET.get('term')
    # users=User.objects.filter(groups__name="PATIENT")
    contex = {}
    disease1 = Disease1.objects.filter(doctor__id=request.user.id)
    disease = []
    for d in disease1:
        # print(d.name)
        disease.append(d.name)
    if search_term == None:
        search_term = ""
    new_predictions = WhoPredictDisease.objects.filter(
        predicted_disease__in=disease).filter(Q(predicted_disease__icontains=search_term) | Q(predict_by__name__icontains=search_term) | Q(predict_by__name__icontains=search_term))
    # print(new_predictions)
    # for p in new_predictions:
    #     print(p.predict_by.address)
    contex = {
        'predictions': new_predictions
    }
    return render(request, 'doctor/dashboard_doctor.html', contex)
    # return render(request,'doctor/dashboard_doctor.html', contex)

    # contex={}
    # # name = request.session.get('username')
    # # user_id = request.session.get('user_id')
    # # if user_id:
    # #     contex={
    # #         'username':name
    # #     }
    # return render(request,'doctor/dashboard_doctor.html', contex)
    # # return render(request,'doctor/dashboard_doctor.html', contex)



"""


def doctor_login(request):
    contex={}
    if request.method == 'POST':
        username = request.POST.get('username')       
        password = request.POST.get('password') 
        user = DoctorInfo.objects.filter(username=username,password=password).first()
        if user:
            request.session['username']=user.username
            request.session['user_id']=user.id
            # return render(request,'doctor/dashboard.html')
            return redirect('dashboard')
        else:
            messages.info(request, "Invalid Username or password")
            doctor_form=DoctorInfoForm()
            contex={}
            return render(request,'doctor/login.html', contex)
    return render(request,'doctor/login.html', contex)

def logout(request):
    user = request.session.get('user_id')
    del user
    return redirect('/')


"""    