from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as dj_login
from doctor.models import DoctorInfo
from django.contrib import messages
from doctor.forms import UserForm
# Create your views here.

def doctor_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        doctor=DoctorInfo.objects.filter(username=username,password=password).first()
        if doctor:
            request.session['username']=username
            context={
            'logged_in':True
            }
            return render(request,'doctor/dashboard.html',context)
        else:
            context={
            'logged_in':False,
            'messages':'Invalid username or password'
            }
            return render(request,'doctor/login.html',context)

    else:
        return render(request,'doctor/login.html')


# def doctor_register(request):
#     doctor_register=UserForm()
#     if request.method == 'POST':
#         doctor_register= UserForm(request.POST)
#         if doctor_register.is_valid():
#             doctor_register.save()
#             return redirect("doctor_login")
#         else:
#             contex={
#                 'doctor_register':doctor_register
#             }
#             print("in valid inputs")
#             return render(request, 'doctor/register.html', contex)
#     else:     
#         doctor_register=UserForm()
#         contex={
#             'doctor_register':doctor_register,
#         }
#         return render(request, 'doctor/register.html', contex)


def logout(request):
    del request.session['username']
    return redirect('/doctor')




"""

def dashboard(request):
    contex={}
    name = request.session.get('username')
    user_id = request.session.get('user_id')
    if user_id:
        contex={
            'username':name
        }
        return render(request,'doctor/dashboard.html', contex)
    return render(request,'doctor/dashboard.html', contex)





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