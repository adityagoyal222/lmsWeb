from rest_framework import serializers

from .models import Assignment, SubmitAssignment
from users.serializers import UserSerializer

class AssignmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Assignment
        fields = ('id', 'assignment_name', 'assignment_description', 'start_date', 'due_date', 'course')
    