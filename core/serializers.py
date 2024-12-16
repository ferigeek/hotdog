from django.contrib.auth.models import Group
from rest_framework.serializers import ModelSerializer
from . import models


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ['name']