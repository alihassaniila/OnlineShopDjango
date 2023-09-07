from django.shortcuts import render
from django.core.cache import cache
import random
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer

class RegisterView(APIView):

    def post(self, request):
        phone_number = request.data.get('phone_number')
        username = request.data.get('username')
        email = request.data.get('email')
        password= request.data.get('password')
        if not phone_number:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(phone_number=phone_number)
        except User.DoesNotExist:
            user = User.objects.create_user(phone_number=phone_number, email=email, username=username, password=password)

        code= random.randint(1000, 9999)
        cache.set(str(phone_number), code, 2 * 60)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class UserListView(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True, context={'request': request})
        return Response(serializer.data)

class UserDetailView(APIView):
    def get(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user, context={'request': request})
        return Response(serializer.data)




