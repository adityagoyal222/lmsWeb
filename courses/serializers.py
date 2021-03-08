from rest_framework import serializers

from .models import Course, Enrollment


class CourseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Course
        fields = "__all__"
        

# class EnrollmentSerializer(serializers.ModelSerializer):
#     course = CourseSerializer(many=True)


#     class Meta:
#         model = Enrollment
#         fields = ('course', 'student')