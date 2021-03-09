from django.http.response import JsonResponse
from .models import User
import requests
from rest_framework import permissions
import requests


class StudentPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == 1

class TeacherPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.user_type == 2