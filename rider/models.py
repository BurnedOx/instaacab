from django.db import models
from django.contrib.auth.models import User
from django.core.cache import cache
from django.conf import settings
import datetime


class RiderProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    profileImage = models.ImageField(upload_to='profile-image', default='profile-image/default.jpeg')

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
