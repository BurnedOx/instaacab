from rest_framework import routers
from .views import *

route = routers.DefaultRouter()

route.register(r'type', VehicleTypeView, base_name='vehicle_type')
route.register(r'vehicles', VehicleView, base_name='vehicle')

urlpatterns = []

urlpatterns += route.urls
