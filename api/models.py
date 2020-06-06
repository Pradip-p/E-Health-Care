from django.db import models

# Create your models here.
class Disease(models.Model):
    Symptom_1=models.CharField(max_length=50)
    Symptom_2=models.CharField(max_length=50)
    Symptom_3=models.CharField(max_length=50, null=True, blank=True)
    def to_dict(self):
        return{
            'Symptom_1':self.Symptom_1,
            'Symptom_2':self.Symptom_2,
            'Symptom_3':self.Symptom_3,
        }