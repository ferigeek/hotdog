from django.urls import path
from task.views import api


urlpatterns = [
    path('tasks', api.TasksView.as_view(), name='list_create_task'),
    path('tasks/<int:id>', api.TaskView.as_view(), name='retrieve_update_destroy_task'),
    path('tasks/<int:id>/history', api.TaskHistoryView.as_view(), name='list_task_history')
]
