from rest_framework import serializers

from .models import Assignment, SubmitAssignment
from users.serializers import UserSerializer

class AssignmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Assignment
        fields = ('id', 'assignment_name', 'assignment_description', 'start_date', 'due_date', 'course')


class SubmitAssignmentSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = SubmitAssignment
        fields = ('id', 'author', 'topic', 'submission_text', 'submission_file', 'submitted_date', 'assignment_ques', 'graded', 'grade')
        