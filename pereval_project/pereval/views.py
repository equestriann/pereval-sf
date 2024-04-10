from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView

from .serializers import *
from .models import *


# class UsersViewset(viewsets.ModelViewSet):
#     queryset = Users.objects.all()
#     serializer_class = UsersSerializer
#
#
# class CoordsViewset(viewsets.ModelViewSet):
#     queryset = Coords.objects.all()
#     serializer_class = CoordsSerializer
#
#
# class LevelViewset(viewsets.ModelViewSet):
#     queryset = Level.objects.all()
#     serializer_class = LevelSerializer
#
#
# class ImageViewset(viewsets.ModelViewSet):
#     queryset = Images.objects.all()
#     serializer_class = ImagesSerializer


class PassViewset(ListCreateAPIView):
    queryset = Pass.objects.all()
    serializer_class = PassSerializer
