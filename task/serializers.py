from rest_framework.serializers import ModelSerializer
from . import models


class TasksSerializer(ModelSerializer):
    class Meta:
        model = models.Task
        fields = '__all__'

    
class TaskSerializer(ModelSerializer):
    class Meta:
        