from rest_framework import routers
from django.urls import path
from .views import *

route = routers.DefaultRouter()

route.register(r'profile', RiderProfileView, base_name='rider_profile')

urlpatterns = [
    path('add-group/', AddRiderGroup.as_view()),
]

urlpatterns += route.urls
