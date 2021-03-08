from rest_framework import urlpatterns
from rest_framework.routers import SimpleRouter

from .views import CourseViewSet

app_name = "courses"
router = SimpleRouter()
router.register(r"courses", CourseViewSet)

urlpatterns = router.urls