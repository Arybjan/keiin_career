from rest_framework import serializers
from users.models import User, Genders


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class GendersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genders
        fields = "__all__"
