from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django.http.response import JsonResponse
from rest_framework.permissions import AllowAny
from rest_framework import serializers

from .serializers import CourseSerializer, EnrollmentSerializer
from .models import Course, Enrollment
from users.permissions import StudentPermission, TeacherPermission

# Create your views here.
class CourseViewSet(ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [AllowAny]
        else:
            permission_classes = [TeacherPermission]
        return [permission() for permission in permission_classes]




class EnrollmentViewSet(ModelViewSet):
    serializer_class = EnrollmentSerializer
    queryset = Enrollment.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [AllowAny]
        else:
            permission_classes = [StudentPermission]
        return [permission() for permission in permission_classes]