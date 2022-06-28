from django.shortcuts import render
from django import views
from rest_framework import viewsets
from crud.models import User
from crud.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer