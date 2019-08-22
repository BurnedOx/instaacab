from rest_framework import routers
from django.urls import path
from .views import *

route = routers.DefaultRouter()

route.register(r'profile', DriverProfileView, base_name='driver_profile')

urlpatterns = [
    path('add-group/', AddDriverGroup.as_view()),
]

urlpatterns += route.urls
