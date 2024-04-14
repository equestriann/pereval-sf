from django.shortcuts import render
from rest_framework import viewsets

from .serializers import *
from .models import *


class PassViewset(viewsets.ModelViewSet):
    """

    """
    queryset = Pass.objects.all()
    serializer_class = PassSerializer
