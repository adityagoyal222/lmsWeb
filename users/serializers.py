from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password', 'user_type')

# class StudentSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Student
#         fields = ('user',)

# class TeacherSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Teacher
#         fields = ('user',)