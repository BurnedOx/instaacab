from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from driver.models import DriverProfile
from rider.models import RiderProfile
from owner.models import OwnerProfile

roll = {
    'owner': OwnerProfile,
    'driver': DriverProfile,
    'rider': RiderProfile,
}


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        token['profileId'] = roll[user.groups.first().name].objects.get(user=user).id
        token['type'] = user.groups.first().name

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
