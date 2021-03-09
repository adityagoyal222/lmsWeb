from rest_framework import serializers

from .models import Course, Enrollment
from users.serializers import UserSerializer

class CourseSerializer(serializers.ModelSerializer):
    teacher = UserSerializer()
    students = UserSerializer(many=True)
    class Meta:
        model = Course
        fields = ('course_name', 'course_description', 'teacher', 'students')
        

class EnrollmentSerializer(serializers.ModelSerializer):
    course = CourseSerializer(many=True)
    student = UserSerializer(many=True)


    class Meta:
        model = Enrollment
        fields = ('course', 'student')