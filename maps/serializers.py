from dataclasses import fields
from rest_framework.serializers import ModelSerializer, IntegerField

from django.contrib.auth.models import User
from maps.models import Map
from pangaea_game_backend.serializers import UserSerializer

class MapSerializer(ModelSerializer):
    owner = UserSerializer(read_only=True)
    user_id = IntegerField(write_only=True)
    class Meta:
        model = Map
        fields = '__all__'
    
    def create(self, validated_data):
        user_id = validated_data.pop('user_id')
        validated_data['owner'] = User.objects.get(id=user_id)
        return super().create(validated_data)
