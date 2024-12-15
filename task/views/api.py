from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from task import serializers, models


class TasksView(ListCreateAPIView):
    serializer_class = serializers.TasksSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return models.Task.objects.filter(related_to__in=user.groups.all()).distinct()