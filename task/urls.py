from django.urls import path, include
from .views import TaskView

urlpatterns = [
    path('<int:task_id>/', TaskView.as_view(), name='task-detail'),
]