from rest_framework import serializers

from .models import Course, Enrollment
from users.serializers import UserSerializer

class CourseSerializer(serializers.ModelSerializer):
    teacher = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Course
        fields = ('id', 'course_name', 'course_description', 'teacher')
    
        

class EnrollmentSerializer(serializers.ModelSerializer):
    student = serializers.HiddenField(default=serializers.CurrentUserDefault())


    class Meta:
        model = Enrollment
        fields = ('id', 'course', 'student')