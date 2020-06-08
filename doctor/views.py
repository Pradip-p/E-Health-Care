from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as dj_login
from doctor.models import DoctorInfo
from django.contrib import messages
# Create your views here.
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