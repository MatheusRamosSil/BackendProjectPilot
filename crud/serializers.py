from pyexpat import model
from attr import fields
from rest_framework import serializers
from crud.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
    