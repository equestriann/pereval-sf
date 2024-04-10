from .models import *
from rest_framework.serializers import ModelSerializer


class UsersSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"


class PassSerializer(ModelSerializer):
    class Meta:
        model = Pass
        fields = [
            'beauty_title',
            'title',
            'other_titles',
            'connect',
            'coord',
            'user',
            'lvl_winter',
            'lvl_spring',
            'lvl_summer',
            'lvl_autumn',
        ]
