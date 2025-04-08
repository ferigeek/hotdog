from django.db import models
from core.models import HotdogUser, Course


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    notify_at = models.DateTimeField()
    completed = models.BooleanField(default=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)
    created_by = models.ForeignKey(HotdogUser, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return f"{self.title} - {self.deadline}"
    
    
class TaskHistory(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    modified_at = models.DateTimeField(auto_now_add=True)
    moddified_by = models.ForeignKey(HotdogUser, on_delete=models.CASCADE, related_name='task_history')
    pre_title = models.CharField(max_length=200, blank=True)
    pre_description = models.TextField(blank=True)
    pre_created_at = models.DateTimeField(auto_now_add=True, blank=True)
    pre_deadline = models.DateTimeField(auto_now_add=True, blank=True)
    pre_notify_at = models.DateTimeField(auto_now_add=True, blank=True)
    pre_completed = models.BooleanField(default=False, blank=True)