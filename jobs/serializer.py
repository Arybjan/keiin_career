from rest_framework import serializers
from jobs.models import Job, CompanyName


class JobsSerializer(serializers.ModelSerializer):
    class Meta:
        models = Job
        fields = "__all__"


class CompanyNameSerializer(serializers.ModelSerializer):
    class Meta:
        models = CompanyName
        fields = "__all__"
