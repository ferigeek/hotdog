from django.urls import path
from . import views


urlpatterns = [
    path('', views.GroupView.as_view(), name='list_create_group')    
]
