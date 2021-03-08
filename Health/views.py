from django.shortcuts import render, HttpResponse
import requests
from Health.forms import DiseaseForm
from api.models import Disease
from api import diseaseml
from Health.decorators import unauthenticated_user

@unauthenticated_user
def index(request):
    return render(request,'Health/index.html')


