from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from task import serializers, models


class TasksView(ListCreateAPIView):
    serializer_class = serializers.TasksSerializer
    queryset = models.Task.objects.all()