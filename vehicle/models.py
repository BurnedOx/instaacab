from django.db import models
from owner.models import OwnerProfile
from driver.models import DriverProfile

vehicle_status_choices = (
    ('Active', 'active'),
    ('Inactive', 'inactive'),
)


class VehicleType(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    vehicleImage = models.ImageField(upload_to='vehicle')
    vehicleActiveImage = models.ImageField(upload_to='vehicle-active')
    status = models.CharField(max_length=20, choices=vehicle_status_choices, default='Inactive')

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    name = models.CharField(max_length=250)
    type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    number = models.CharField(max_length=100)
    owner = models.ForeignKey(OwnerProfile, on_delete=models.CASCADE)
    driver = models.ForeignKey(DriverProfile, on_delete=models.CASCADE)
    insuranceCertificate = models.ImageField(upload_to='vehicle-insurance')
    registrationCertificate = models.ImageField(upload_to='vehicle-registration')
    carriagePermit = models.ImageField(upload_to='vehicle-permit')
    status = models.CharField(max_length=20, choices=vehicle_status_choices, default='Inactive')

    def __str__(self):
        return self.name
