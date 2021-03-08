from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .serializers import CourseSerializer
from .models import Course

# Create your views here.
class CourseViewSet(ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()