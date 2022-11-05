from rest_framework import viewsets
from jobs.models import Job, CompanyName
from jobs.serializer import JobsSerializer, CompanyNameSerializer


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobsSerializer


class CompanyNameViewSet(viewsets.ModelViewSet):
    queryset = CompanyName.objects.all()
    serializer_class = CompanyNameSerializer
