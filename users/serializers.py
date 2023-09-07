from rest_framework import serializers
from .models import User
class UserSerializer(serializers.ModelSerializer):
    model = User
    class Meta:
        model = User
        fields = ('id','phone_number', 'username', 'email', 'password','is_staff')