from django.shortcuts import render

# Create your views here.'
from rest_framework import generics

from maps.models import Map
from maps.serializers import MapSerializer


class MapListCreate(generics.ListCreateAPIView):
    queryset = Map.objects.all()
    serializer_class = MapSerializer

class MapRetrieveDelete(generics.RetrieveDestroyAPIView):
    queryset = Map.objects.all()
    serializer_class = MapSerializer
