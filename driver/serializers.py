from rest_framework import serializers
from .models import *


class DriverProfileSerializer(serializers.ModelSerializer):
    firstName = serializers.ReadOnlyField()
    lastName = serializers.ReadOnlyField()
    email = serializers.ReadOnlyField()
    lastSeen = serializers.ReadOnlyField()
    online = serializers.ReadOnlyField()

    class Meta:
        model = DriverProfile
        fields = '__all__'
