from django.shortcuts import render
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from .serializers import ResourceSerializer
from .models import Resource
from users.permissions import StudentPermission, TeacherPermission

# Create your views here.
class ResourceViewSet(ModelViewSet):
    serializer_class = ResourceSerializer
    queryset = Resource.objects.all()

    def get_permissions(self):
        if self.request.method == "GET":
            permission_classes = [AllowAny]
        else:
            permission_classes = [TeacherPermission]
        return [permission() for permission in permission_classes]

    def pre_save(self, obj):
        obj.resource_file = self.request.FILES.get('file')