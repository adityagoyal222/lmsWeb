from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.permissions import AllowAny
from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework import generics
from rest_framework.views import APIView

from .models import User
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
        user.save()
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def profile(request):
    user = request.user
    serialized_user = UserSerializer(user).data
    return Response({'user': serialized_user})

# @api_view(['POST'])
# @permission_classes([AllowAny])
# @ensure_csrf_cookie
# def login_view(request):
#     username = request.data.get('username')
#     password = request.data.get('password')
#     response = Response()
#     if(username is None) or (password is None):
#         raise exceptions.AuthenticationFailed('username and password required')

#     user = User.objects.filter(username=username).first()
#     if(user is None):
#         raise exceptions.AuthenticationFailed('user not found')
#     if (not user.check_password(password)):
#         raise exceptions.AuthenticationFailed('wrong password')

#     serialized_user = UserSerializer(user).data

#     access_token = generate_access_token(user)
#     refresh_token = generate_refresh_token(user)

#     response.set_cookie(key='refreshtoken', value=refresh_token, httponly=True)
#     response.data = {
#         'access_token': access_token,
#         'user': serialized_user,
#     }

#     return response


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer