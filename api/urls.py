from django.conf.urls import url
from rest_framework import urlpatterns
from rest_framework.routers import SimpleRouter

from courses.views import CourseViewSet
from users.views import create_auth, login

app_name = "api"
router = SimpleRouter()
router.register(r"courses", CourseViewSet)

urlpatterns = router.urls
urlpatterns += [
    url(r'^users/register', create_auth, name="register"),
    url(r'^users/login', login, name="login"),
]