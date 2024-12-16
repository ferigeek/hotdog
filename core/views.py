from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.models import Group
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from . import models, serializers


class GroupView(ListCreateAPIView):
    serializer_class = serializers.GroupSerializer
    permission_classes = [IsAuthenticated]
    queryset = Group.objects.all()

    def perform_create(self, serializer):
        group = serializer.save()

        models.GroupMeta.objects.create(
            group=group, 
            created_at=datetime.now(), 
            created_by=self.request.user
        )
