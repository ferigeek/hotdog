from django.urls import path, include
from .views import TaskView, TaskHistoryView, TaskCreateView, TaskListView

urlpatterns = [
    path('<int:task_id>/', TaskView.as_view(), name='task-detail'),
    path('<int:task_id>/history/', TaskHistoryView.as_view(), name='task-history'),
    path('', TaskCreateView.as_view(), name='task-create'),
    path('me/', TaskListView.as_view(), name='task-list'),
]