from django import forms
from api.models import Disease
from patient.models import Heart, Diabetes, Image

class ImageForm(forms.ModelForm):
    class Meta:
        model= Image
        fields= ["imagefile"]
from patient.models import Heart, Diabetes



class DiabetesForm(forms.ModelForm):
    class Meta():
        model = Diabetes
        fields='__all__'
      

class DiseaseForm(forms.ModelForm):
    class Meta():
        model = Disease
        fields='__all__'
class HeartForm(forms.ModelForm):
    class Meta():
        model = Heart
        fields='__all__'
        # labels = {
        #     'age': (' Your age'),
        #     'sex': ("sex : 1: male, 0: Female"),
        #     'cp':("cp :Chest pain type"),
        #     'chol' : ("chol :Serum cholestoral in mg/dl : "),
        #     'exang':('exercise induced angina (1 = yes; 0 = no)'),
        #     'thalach':("thalach :maximum heart rate achieved"),
        #     'fbs':("fbs :(fasting blood sugar &gt; 120 mg/dl) (1 = true; 0 = false)"),
        #     'trestbps':("trestbps :resting blood pressure (in mm Hg on admission to the hospital)"),
        #     'restecg':("restecg : resting electrocardiographic results"),
        #     'oldpeak': (" oldpeak : ST depression induced by exercise relative to rest"),
        #     'thal': ("thal: 0 = normal; 1 = fixed defect; 2 = reversable defect")
        # }
    
