import datetime
from django.conf import settings
from django.core.cache import cache
from .models import RiderProfile


class ActiveRiderMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            now = datetime.datetime.now()
            current_user = request.user
            if len(current_user.groups.all()) == 1 and current_user.groups.all()[0].name == 'rider':
                try:
                    RiderProfile.objects.get(user=current_user)
                except RiderProfile.DoesNotExist:
                    RiderProfile.objects.create(user=current_user)
                finally:
                    cache.set('last_seen_%s' % current_user.username, now,
                              settings.USER_LASTSEEN_TIMEOUT)
        response = self.get_response(request)
        return response
