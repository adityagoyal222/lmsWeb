from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django.http.response import JsonResponse

from .serializers import CourseSerializer, EnrollmentSerializer
from .models import Course, Enrollment
from users.permissions import StudentPermission, TeacherPermission

# Create your views here.
class CourseViewSet(ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [TeacherPermission]




class EnrollmentViewSet(ModelViewSet):
    serializer_class = EnrollmentSerializer
    queryset = Enrollment.objects.all()
    permission_classes = [StudentPermission]