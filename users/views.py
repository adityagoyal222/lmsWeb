from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework import generics
from rest_framework.views import APIView

from .models import Student, Teacher, User
from .serializers import UserSerializer


# Create your views here.
@api_view(['POST'])
def create_auth(request):
    serialized = UserSerializer(data=request.data)
    if serialized.is_valid():
        user = User.objects.create(
            username = request.data.get('username'),
            email = request.data.get('email'),
            first_name = request.data.get('first_name'),
            last_name = request.data.get('last_name'),
            user_type = request.data.get('user_type'),
        )
        user.set_password(request.data.get('password'))
        if user.user_type == "1":
            student = Student.objects.create(user=user)
            student.save()
        elif user.user_type == "2":
            teacher = Teacher.objects.create(user=user)
            teacher.save()
        user.save()
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    print(username)
    print(password)
    user = authenticate(username=username, password=password)
    print(User.objects.get(username=username).password)
    if not user:
        return Response({"error": "Login failed"}, status=status.HTTP_401_UNAUTHORIZED)

    token, _ = Token.objects.get_or_create(user=user)
    return Response({"token": token.key})


class LogoutView(APIView):
    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer