from django.shortcuts import render, HttpResponse
import requests
from Health.forms import DiseaseForm
from api.models import Disease
from api import diseaseml


def index(request):
    """if request.method=="GET":
        disease_form=DiseaseForm(request.POST)
        response = requests.get("http://127.0.0.1:8000/api/api/api/10")
        data = response.json()
        # return HttpResponse("Hello World!")
        return render(request,'Health/index.html', {
            # 'Symptom_1': data['Symptom_1'],
            # 'Symptom_2': data['Symptom_2'],
            # 'Symptom_3': data['Symptom_3'],
            'disease_form':disease_form
        }
        )
    elif request.method=="POST":
        disease_form=DiseaseForm(request.POST)
        if disease_form.is_valid:
            disease_form.save()
            ob=Disease.objects.latest('id')
            sur=diseaseml.pred(ob)
            contex={"Disease":sur}
    return render(request,'Health/index.html', contex)"""

    return render(request,'Health/index.html')


