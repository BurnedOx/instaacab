from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import datetime
from django.core.cache import cache

profile_status_choices = (
    ('Active', 'active'),
    ('Inactive', 'inactive'),
    ('Pending', 'pending'),
)


class OwnerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    vatNumber = models.CharField(max_length=250, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=20, choices=profile_status_choices, default='Pending')
    address = models.CharField(max_length=250, blank=True, null=True)
    city = models.CharField(max_length=250, blank=True, null=True)
    state = models.CharField(max_length=250, blank=True, null=True)
    pinCode = models.CharField(max_length=250, blank=True, null=True)
    profileImage = models.ImageField(upload_to='profile-image', default='profile-image/default.jpeg')
    license = models.ImageField(blank=True, null=True, upload_to='licence')
    licenseExp = models.DateField(blank=True, null=True)
    insurance = models.ImageField(blank=True, null=True, upload_to='insurance')
    insuranceExp = models.DateField(blank=True, null=True)
    commission = models.FloatField(blank=True, null=True)

    @property
    def firstName(self):
        return self.user.first_name

    @property
    def lastName(self):
        return self.user.last_name

    @property
    def email(self):
        return self.user.email

    def lastSeen(self):
        return cache.get('last_seen_%s' % self.user.username)

    def online(self):
        if self.lastSeen():
            now = datetime.datetime.now()
            if now > (self.lastSeen() + datetime.timedelta(seconds=settings.USER_ONLINE_TIMEOUT)):
                return False
            else:
                return True
        else:
            return False

    def __str__(self):
        return self.user.username
