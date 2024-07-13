from django.shortcuts import render
from Health.decorators import unauthenticated_user

@unauthenticated_user
def index(request):
    return render(request,'Health/index.html')


