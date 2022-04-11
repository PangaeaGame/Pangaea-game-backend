from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    model = User
    fields = ['email', 'first_name', 'lastname', 'date_joined']
    