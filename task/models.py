from django.db import models
from django.contrib.auth.models import Group
from core.models import User


class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tasks')
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    notify_at = models.DateTimeField()
    related_to = models.ManyToManyField(Group, related_name='related_tasks')

    def __str__(self):
        return self.title


class TaskHistory(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='modified_tasks')
    modified_at = models.DateTimeField(auto_now_add=True)
    prev_title = models.CharField(max_length=50, blank=True, null=True)
    prev_description = models.TextField(blank=True, null=True)
    prev_deadline = models.DateTimeField(blank=True, null=True)
    prev_notify = models.DateTimeField(blank=True, null=True)
    prev_groups = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.task

