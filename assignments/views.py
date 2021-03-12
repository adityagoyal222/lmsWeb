from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from .serializers import AssignmentSerializer, SubmitAssignmentSerializer
from .models import Assignment, SubmitAssignment
from users.permissions import StudentPermission, TeacherPermission

# Create your views here.
class AssignmentViewSet(ModelViewSet):
    serializer_class = AssignmentSerializer
    queryset = Assignment.objects.all()

    def get_permissions(self):
        if self.request.method == "GET":
            permission_classes = [AllowAny]
        else:
            permission_classes = [TeacherPermission]

        return [permission() for permission in permission_classes]
