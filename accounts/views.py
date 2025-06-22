from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated


# Create your views here.
@api_view(['POST'])
def signup_view(request):
    username = request.data.get("username")
    email = request.data.get("email")
    password = request.data.get("password")
    confirm_password = request.data.get("confirm_password")
    # hajar will  check this in the frontend 

    # if not all([username, email, password, confirm_password]):
    #     return Response({'error' : 'all fields are required'}, status=status.http_400_BAD_REQUEST)
    # if password != confirm_password:
    #     return Response({'error' : 'passwords do not match'}, status=status.http_400_BAD_REQUEST)
    if User.objects.filter(email=email).exists():
        return Response({'error': 'a user with the same email already exists'}, status=status.HTTP_400_BAD_REQUEST)
    user = User.objects.create_user(username=username, email=email, password=password)
    return Response({"message" : "User created succeessfully"}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def signin_view(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(username=username, password=password)
    if not user:
        return Response({"error": "invalid credentials"}, status=401)
    return Response({"message" : "login successful"}, status=200)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_users(request):
    users = User.objects.all()
    data = []
    for user in users :
        data.append(
            {
                'id' : user.id,
                'email':user.email,
                'username' : user.username
            }
        )
    return Response(data)