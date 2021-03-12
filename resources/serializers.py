from rest_framework import serializers

from .models import Resource
from courses.serializers import Course

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ('id', 'resource_name', 'resource_file', 'course')