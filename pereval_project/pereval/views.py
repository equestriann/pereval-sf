from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView, ListAPIView, CreateAPIView

from .serializers import *
from .models import *


class PassCreate(ListCreateAPIView):
    """
    DRF generic View representing the list of passes in DB
    And a POST form for creating new Pass Model object
    """
    queryset = Pass.objects.all()
    serializer_class = PassSerializer
