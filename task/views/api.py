import json
from datetime import datetime
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from task import serializers, models, permissions


class TasksView(ListCreateAPIView):
    serializer_class = serializers.TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return models.Task.objects.filter(related_to__in=user.groups.all()).distinct()
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    

class TaskView(RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.TaskPermission]
    queryset = models.Task.objects.all()
    lookup_field = 'id'
    serializer_class = serializers.TaskSerializer

    def delete(self, request, *args, **kwargs):
        task = models.Task.objects.get(pk=kwargs['id'])
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
    
    def put(self, request, *args, **kwargs):
        task = models.Task.objects.get(pk=kwargs['id'])

        serializer = serializers.TaskSerializer(task, data=request.data)

        if serializer.is_valid():
            prev_title = task.title if task.title != serializer.validated_data.get('title', task.title) else None
            prev_description = task.description if task.description != serializer.validated_data.get('description', task.description) else None
            prev_deadline = task.deadline if task.deadline != serializer.validated_data.get('deadline', task.deadline) else None
            prev_notify = task.notify_at if task.notify_at != serializer.validated_data.get('notify_at', task.notify_at) else None
            prev_groups = json.dumps([group.id for group in task.related_to.all()]) if serializer.validated_data.get('related_to', None) != [group.id for group in task.related_to.all()] else None

            serializer.save()

            history = models.TaskHistory.objects.create(
                task=task,
                modified_by=request.user,
                modified_at=datetime.now(),
                prev_title=prev_title,
                prev_description=prev_description,
                prev_deadline=prev_deadline,
                prev_notify=prev_notify,
                prev_groups=prev_groups,
            )

        return super().put(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        task = models.Task.objects.get(pk=kwargs['id'])

        serializer = serializers.TaskSerializer(task, data=request.data, partial=True)

        if serializer.is_valid():
            prev_title = task.title if 'title' in request.data and task.title != serializer.validated_data.get('title', task.title) else None
            prev_description = task.description if 'description' in request.data and task.description != serializer.validated_data.get('description', task.description) else None
            prev_deadline = task.deadline if 'deadline' in request.data and task.deadline != serializer.validated_data.get('deadline', task.deadline) else None
            prev_notify = task.notify_at if 'notify_at' in request.data and task.notify_at != serializer.validated_data.get('notify_at', task.notify_at) else None
            prev_groups = json.dumps([group.id for group in task.related_to.all()]) if 'related_to' in request.data and serializer.validated_data.get('related_to', None) != [group.id for group in task.related_to.all()] else None

            serializer.save()

            history = models.TaskHistory.objects.create(
                task=task,
                modified_by=request.user,
                modified_at=datetime.now(),
                prev_title=prev_title,
                prev_description=prev_description,
                prev_deadline=prev_deadline,
                prev_notify=prev_notify,
                prev_groups=prev_groups,
            )

        return super().patch(request, *args, **kwargs)
    

class TaskHistoryView(ListAPIView):
    serializer_class = serializers.TaskHistorySerializer
    permission_classes = [permissions.TaskPermission]
    queryset = models.TaskHistory.objects.all()

    def get_queryset(self):
        return models.TaskHistory.objects.filter(task=self.kwargs['id'])