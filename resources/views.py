from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from .serializers import ResourceSerializer
from .models import Resource
from users.permissions import StudentPermission, TeacherPermission

# Create your views here.
class ResourceViewSet(ModelViewSet):
    pass