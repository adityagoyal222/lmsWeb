from django.conf.urls import include, url
from rest_framework import urlpatterns
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from courses.views import CourseViewSet, EnrollmentViewSet
from users.views import create_auth, UserList

app_name = "api"
router = SimpleRouter()
router.register(r"courses", CourseViewSet)
router.register(r"enroll", EnrollmentViewSet)

urlpatterns = [
    url('', include(router.urls)),
    url(r'^users/$', UserList.as_view()),
    url(r'^users/register', create_auth, name="register"),
    # url(r'^users/login', login, name="login"),
    # url(r'^users/logout/', LogoutView.as_view(), name="logout"),
    url(r'^token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]