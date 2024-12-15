from datetime import datetime
import json
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from task import serializers, models, permissions


class TasksView(ListCreateAPIView):
    serializer_class = serializers.TasksSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return models.Task.objects.filter(related_to__in=user.groups.all()).distinct()
    

class TaskView(RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.TaskPermission]
    queryset = models.Task.objects.all()
    lookup_field = 'id'
    serializer_class = serializers.TaskSerializer

    def delete(self, request, *args, **kwargs):
        task = models.Task.objects.get(pk=id)
        groups = [group.id for group in task.related_to.all()]
        history = models.TaskHistory.objects.create(
            task = task,
            modified_by = request.user,
            modified_at = datetime.now(),
            prev_title = task.title,
            prev_description = task.description,
            prev_deadline = task.deadline,
            prev_notify = task.notify_at,
            prev_groups = json.dumps(groups)
        )
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
