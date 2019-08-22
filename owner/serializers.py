from rest_framework import serializers
from .models import *


class OwnerProfileSerializer(serializers.ModelSerializer):
    firstName = serializers.ReadOnlyField()
    lastName = serializers.ReadOnlyField()
    email = serializers.ReadOnlyField()
    lastSeen = serializers.ReadOnlyField()
    online = serializers.ReadOnlyField()

    class Meta:
        model = OwnerProfile
        fields = '__all__'
