from django.http import HttpResponse
from django.shortcuts import redirect

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request,*args,**kwargs):
            group=None
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request,*args,**kwargs)
            else:
                return HttpResponse("You are not authorized to access this page")
        return wrapper_func
    return decorator

def unauthenticated_admin(view_func):
    def wrapper_fun(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('admin_dashboard')
        else:
            return view_func(request,*args,**kwargs)
    return wrapper_fun

