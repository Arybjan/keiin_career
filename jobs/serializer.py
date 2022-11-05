from rest_framework import serializers
from jobs import models


class JobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Job
        fields = "__all__"


class CompanyNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CompanyName
        fields = "__all__"
