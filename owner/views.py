from rest_framework import viewsets, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .serializers import *
from instaacab.utils import get_roll


class OwnerProfileView(viewsets.ModelViewSet):
    queryset = OwnerProfile.objects.all()
    serializer_class = OwnerProfileSerializer


class AddOwnerGroup(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        username = request.data['username']
        if username is not None:
            user = User.objects.get(username=username)
            user.groups.add(get_roll('owner'))
            return Response('Owner group added', status=status.HTTP_200_OK)
        return Response('Must provide username', status=status.HTTP_400_BAD_REQUEST)
