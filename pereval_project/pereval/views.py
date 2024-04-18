from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from drf_yasg.utils import swagger_auto_schema

from .serializers import *
from .models import *


class PassViewset(viewsets.ModelViewSet):
    """
    Viewset provides pass data management:
    Allows creating, updating and viewing pass information

    Attributes:
        queryset (QuerySet): Set of Pass model objects available for queries
        serializer_class (Serializer): Serializer used for converting Pass objects to and from JSON
        filterset_fields (list): List of fields by which the Pass object set can be filtered

    Methods:
        create(self, request, *args, **kwargs): Method for creating new pass object
        partial_update(self, request, *args, **kwargs): Method for partial update of an existing pass
    """
    queryset = Pass.objects.all()
    serializer_class = PassSerializer
    filterset_fields = ['tourist__email']

    def create(self, request, *args, **kwargs):
        """
        Parent class method override to handle object creating result

        :param request: HttpRequest object containing pass data.
        :type request: HttpRequest
        :return: JSON response with the result of the pass creation operation.
        :rtype: Response
        """
        serializer = PassSerializer(data=request.data)
        if serializer.is_valid():
            return Response({
                "status": status.HTTP_200_OK,
                "message": None,
                "id": serializer.data['id'],
            })
        if status.HTTP_400_BAD_REQUEST:
            return Response({
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "Bad Request",
                "id": None,
            })
        if status.HTTP_500_INTERNAL_SERVER_ERROR:
            return Response({
                "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "message": "Database connection error",
                "id": None,
            })

    def partial_update(self, request, *args, **kwargs):
        """
        Parent class method override to handle object update result

        :param request: HttpRequest object containing pass update data.
        :type request: HttpRequest
        :return: JSON response with the result of the pass update operation.
        :rtype: Response
        """
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

    """ Disabling unused parent class methods """
    @swagger_auto_schema(auto_schema=None)
    def update(self, request, *args, **kwargs):
        pass

    @swagger_auto_schema(auto_schema=None)
    def retrieve(self, request, *args, **kwargs):
        pass

    @swagger_auto_schema(auto_schema=None)
    def destroy(self, request, *args, **kwargs):
        pass
