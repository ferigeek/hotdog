from django.shortcuts import render
from django.utils import timezone
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import TaskSerializer, TaskHistorySerializer
from .models import Task, TaskHistory


class TaskView(APIView):
    """
    API endpoint to observe and modify a single task.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, task_id):
        """
        Retrieve a task by its ID.
        """
        try:
            task = Task.objects.get(id=task_id)
            serializer = TaskSerializer(task)
            return Response(serializer.data)
        except Task.DoesNotExist:
            return Response(status=404)

    def put(self, request, task_id):
        """
        Update a task by its ID.
        """
        try:
            task = Task.objects.get(id=task_id)
            serializer = TaskSerializer(task, data=request.data)
            if serializer.is_valid():
                # Save a history record before modification
                TaskHistory.objects.create(
                    task=task,
                    modified_at=timezone.now(),
                    moddified_by=request.user,
                    pre_title=task.title,
                    pre_description=task.description,
                    pre_created_at=task.created_at,
                    pre_deadline=task.deadline,
                    pre_notify_at=task.notify_at,
                    pre_completed=task.is_finished
                )
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        except Task.DoesNotExist:
            return Response(status=404)

    def patch(self, request, task_id):
        """
        Partially update a task by its ID.
        """
        try:
            task = Task.objects.get(id=task_id)
            serializer = TaskSerializer(task, data=request.data, partial=True)
            if serializer.is_valid():
                # Save a history record before modification
                TaskHistory.objects.create(
                    task=task,
                    modified_at=timezone.now(),
                    moddified_by=request.user,
                    pre_title=task.title,
                    pre_description=task.description,
                    pre_created_at=task.created_at,
                    pre_deadline=task.deadline,
                    pre_notify_at=task.notify_at,
                    pre_completed=task.is_finished
                )
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        except Task.DoesNotExist:
            return Response(status=404)
        
    def delete(self, request, task_id):
        """
        Delete a task by its ID.
        """
        try:
            task = Task.objects.get(id=task_id)
            # Save a history record before deletion
            TaskHistory.objects.create(
                    task=task,
                    modified_at=timezone.now(),
                    moddified_by=request.user,
                    pre_title=task.title,
                    pre_description=task.description,
                    pre_created_at=task.created_at,
                    pre_deadline=task.deadline,
                    pre_notify_at=task.notify_at,
                    pre_completed=task.is_finished,
                    got_deleted=True
                )
            task.delete()
            return Response(status=204)
        except Task.DoesNotExist:
            return Response(status=404)