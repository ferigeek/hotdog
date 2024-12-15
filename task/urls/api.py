from django.urls import path
from task.views import api


urlpatterns = [
    path('tasks', api.TasksView.as_view(), name='list_create_task'),
    # path('tasks/<int:id>')
]
