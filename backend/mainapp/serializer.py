from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo    #The model that we want to serialize
        exclude = ['created_at', 'updated_at'] #We don't want to show these fields in the API response