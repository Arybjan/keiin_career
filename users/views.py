from rest_framework import viewsets
from users.serializer import UserSerializer, GendersSerializer
from users.models import User, Genders


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GendersViewSet(viewsets.ModelViewSet):
    queryset = Genders.objects.all()
    serializer_class = GendersSerializer
