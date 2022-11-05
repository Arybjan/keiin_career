from rest_framework.routers import DefaultRouter
from jobs.views import JobViewSet, CompanyNameViewSet

router = DefaultRouter()

router.register("jobs", JobViewSet)
router.register("company-name", CompanyNameViewSet)

urlpatterns = router.urls
