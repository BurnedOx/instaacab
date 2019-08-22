from rest_framework import viewsets
from .serializers import *


class VehicleTypeView(viewsets.ModelViewSet):
    queryset = VehicleType.objects.all()
    serializer_class = VehicleTypeSerializer


class VehicleView(viewsets.ModelViewSet):
    serializer_class = VehicleSerializer

    def get_queryset(self):
        queryset = Vehicle.objects.all()
        owner_id = self.request.query_params.get('ownerId', None)
        driver_id = self.request.query_params.get('driverId', None)
        status = self.request.query_params.get('status', None)
        if owner_id is not None:
            queryset = queryset.filter(owner=OwnerProfile.objects.get(id=int(owner_id)))
        if driver_id is not None:
            queryset = queryset.filter(driver=DriverProfile.objects.get(id=int(driver_id)))
        if status is not None:
            queryset = queryset.filter(status=status)
        return queryset
