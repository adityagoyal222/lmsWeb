from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .serializers import CourseSerializer, EnrollmentSerializer
from .models import Course, Enrollment

# Create your views here.
class CourseViewSet(ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class EnrollmentViewSet(ModelViewSet):
    serializer_class = EnrollmentSerializer
    queryset = Enrollment.objects.all()