from requests import patch
from rest_framework import routers
from crud.views import UserViewSet
from django.urls import path,include

router = routers.DefaultRouter()
router.register(r'users',UserViewSet)

urlpatterns =[
    path('',include(router.urls))
]