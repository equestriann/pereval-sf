from django.shortcuts import render
from rest_framework import generics

from .serializers import *
from .models import *


class PassList(generics.ListAPIView):
    """
    List View for reading data with GET request
    Returns a list of Pass Model objects
    """

    queryset = Pass.objects.all()
    serializer_class = PassSerializer


class PassCreate(generics.ListCreateAPIView):
    """
    Create View for inserting new passes' data into database
    Returns a POST form for Pass Model
    """

    queryset = Pass.objects.all()
    serializer_class = PassSerializer
