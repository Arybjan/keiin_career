from rest_framework import viewsets
from jobs.models import Job, CompanyName


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
