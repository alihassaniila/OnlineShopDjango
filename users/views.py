from django.shortcuts import render
from django.core.cache import cache
import random
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import User


class RegisterView(APIView):

    def post(self, request):
        phone_number = request.data.get('phone_number')

        if not phone_number:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(phone_number=phone_number)
        except User.DoesNotExist:
            user = User.objects.create_user(phone_number=phone_number, email=phone_number, username=phone_number)

        code= random.randint(1000, 9999)
        cache.set(str(phone_number), code, 2 * 60)
        return Response({'code': code})

