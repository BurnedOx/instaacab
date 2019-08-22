from rest_framework import routers
from django.urls import path
from .views import *

route = routers.DefaultRouter()

route.register(r'profile', OwnerProfileView, base_name='owner_profile')

urlpatterns = [
    path('add-group/', AddOwnerGroup.as_view()),
]

urlpatterns += route.urls
