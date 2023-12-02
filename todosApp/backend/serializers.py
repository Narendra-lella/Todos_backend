from .models import Totomodel
from rest_framework import serializers



class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Totomodel
        fields = '__all__'