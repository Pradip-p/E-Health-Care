from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_fun(request,*args,**kwargs):
        group=None
        if request.user.groups.exists():
            group=request.user.groups.all()[0].name
        if group =='PATIENT':
            return redirect('home')
        elif group=='DOCTOR':
            return redirect('dashboard_doctor')
        elif group=='ADMIN':
            return redirect('admin_dashboard')
        else:
            return view_func(request,*args,**kwargs)
    return wrapper_fun
