from rest_framework import serializers
from api.models import Disease
# from django.contrib.auth.models import User




class DiseaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Disease
        fields='__all__'

