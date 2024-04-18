from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from .serializers import *
from .models import *


class PassViewset(viewsets.ModelViewSet):
    queryset = Pass.objects.all()
    serializer_class = PassSerializer
    filterset_fields = ['tourist__email']

    def partial_update(self, request, *args, **kwargs):
        cur_pass = self.get_object()
        if cur_pass.status == "new":
            serializer = PassSerializer(cur_pass, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "status": 1,
                    "message": "Update successfull"
                })
            else:
                return Response({
                    "state": 0,
                    "message": serializer.errors
                })
        else:
            return Response({
                "status": 0,
                "message": f"Unable to update in status: {cur_pass.get_status_display()}"
            })

    def update(self, request, *args, **kwargs):
        pass

    def retrieve(self, request, *args, **kwargs):
        pass
