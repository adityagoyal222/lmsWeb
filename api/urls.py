from django.conf.urls import include, url
from rest_framework import urlpatterns
from rest_framework.routers import SimpleRouter

from courses.views import CourseViewSet, EnrollmentViewSet
from users.views import LogoutView, create_auth, login, UserList

app_name = "api"
router = SimpleRouter()
router.register(r"courses", CourseViewSet)
router.register(r"enroll", EnrollmentViewSet)

urlpatterns = [
    url('', include(router.urls)),
    url(r'^users/$', UserList.as_view()),
    url(r'^users/register', create_auth, name="register"),
    url(r'^users/login', login, name="login"),
    url(r'^users/logout/', LogoutView.as_view(), name="logout")
]