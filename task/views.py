from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from . import serializers


class TasksView(ListCreateAPIView):
    serializer_class = serializers.TasksSerializer

