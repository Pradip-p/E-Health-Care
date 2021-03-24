from django.db import models

# Create your models here.
class Disease(models.Model):
    value_1 = models.CharField(max_length = 50)
    value_2 = models.CharField(max_length = 50)
    value_3 = models.CharField(max_length = 50)
    value_4 = models.CharField(max_length = 50)
    value_5 = models.CharField(max_length = 50)
    value_6 = models.CharField(max_length = 50)


    def to_dict(self):
        return{
            'value_1': self.value_1,
            'value_2': self.value_2,
            'value_3': self.value_3,
            'value_4': self.value_4,
            'value_5': self.value_5,
            'value_6': self.value_6
        }
  