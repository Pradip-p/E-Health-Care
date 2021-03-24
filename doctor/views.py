from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from doctor.models import DoctorInfo
from django.contrib import messages
from doctor.forms import UserForm
from appointment.forms import AddAppointmentForm
from django.db.models import Q

from django.contrib.auth.decorators import user_passes_test, login_required

from patient.models import Disease1, WhoPredictDisease
# Create your views here.
from doctor.doctor_decorators import unauthenticated_doctor,allowed_users
from django.contrib.auth.decorators import login_required

from appointment.models import AppointmentDetails,BookedAppointment


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
    contex = {}
    from doctor.models import DoctorInfo
    doctor=DoctorInfo.objects.filter(user__id=request.user.id)
    doctorID=[]
    for i in doctor:
        doctorID.append(i.id)
  
    disease1 = Disease1.objects.filter(doctor__id__in=doctorID)
    print(disease1)
    disease = []
    for d in disease1:
        disease.append(d.name)
    if search_term == None:
        search_term = ""
    new_predictions = WhoPredictDisease.objects.filter(
        predicted_disease__in=disease).filter(Q(predicted_disease__icontains=search_term) | Q(predict_by__name__icontains=search_term) | Q(predict_by__name__icontains=search_term))
   
    contex = {
        'predictions': new_predictions
    }
    return render(request, 'doctor/dashboard_doctor.html', contex)

# Apoointement Portion for doctor views..........................

@login_required(login_url='doctor_login')
@allowed_users(allowed_roles=['DOCTOR'])
def appointment(request):
    context={}
    from appointment.models import AppointmentDetails
    appointments=AppointmentDetails.objects.filter(create_by=request.user.doctorinfo)
    context={
        'appointments':appointments
    }
    return render(request,'doctor/appointments.html',context)


@login_required(login_url='doctor_login')
@allowed_users(allowed_roles=['DOCTOR'])
def add_appointment(request):
    if request.method=='POST':
        appointment_add_form=AddAppointmentForm(request.POST or None,request.FILES or None)
        if appointment_add_form.is_valid():
            add_appointment=appointment_add_form.save(commit=False)
            add_appointment.create_by=request.user.doctorinfo
            add_appointment.save()
            return redirect('appointment')
        else:
            context={
                'appointment_add_form':appointment_add_form
            }
            return render(request,'doctor/add_appointment.html',context)
    else:
        appointment_add_form=AddAppointmentForm()
        context={
            'appointment_add_form':appointment_add_form
        }
        return render(request,'doctor/add_appointment.html',context)

@login_required(login_url='doctor_login')
@allowed_users(allowed_roles=['DOCTOR'])
def edit_appointment(request,pk):
    try:
        appointment=AppointmentDetails.objects.get(id=pk,create_by=request.user.doctorinfo)
    except:
        return redirect('appointment')
    if request.method=='POST':   
        appointment_edit_form=AddAppointmentForm(request.POST or None,request.FILES,instance=appointment)
        if appointment_edit_form.is_valid():
            update=appointment_edit_form.save(commit=False)
            update.uploaded_by=request.user.doctorinfo
            update.save()
            return redirect('appointment')
        else:
            context={
                'appointment_edit_form':appointment_edit_form,
                'appointment':appointment
            }
            return render(request,'doctor/appointment_edit_form.html',context)
    else:
        appointment_edit_form=AddAppointmentForm(request.POST or None,request.FILES,instance=appointment)
        context={
            'appointment_edit_form':appointment_edit_form,
            'appointment':appointment
        }
        return render(request,'doctor/appointment_edit_form.html',context)

@login_required(login_url='doctor_login')
@allowed_users(allowed_roles=['DOCTOR'])
def delete_appointment(request,pk):
    print(pk)
    try:
        appointment=AppointmentDetails.objects.get(id=pk,create_by=request.user.doctorinfo)
        appointment.delete()
    except:
        # pass
        return redirect('appointment')
    return redirect('appointment')

@login_required(login_url='doctor_login')
@allowed_users(allowed_roles=['DOCTOR'])
def book_appointment(request):
    appointment=AppointmentDetails.objects.filter(create_by=request.user.doctorinfo)
    print(appointment)
    ID=[]
    for a in appointment:
        ID.append(a.id)
        print(a.id)
    booked_appointments=BookedAppointment.objects.filter(appointment_id__in=ID)
    context={
        'appointments':booked_appointments
    }
    return render(request,'doctor/booked_appointments.html',context)
    print(booked_appointments)
    # booked_appointments=BookedAppointment.objects.filter(appointment_id.create_by=request.user.doctorinfo)
    # print(booked_appointments)

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