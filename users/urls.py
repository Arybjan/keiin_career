from rest_framework.routers import DefaultRouter
from users import views

router = DefaultRouter()

router.register("user", views.UserViewSet)
router.register("gender", views.GendersViewSet)

urlpatterns = router.urls
