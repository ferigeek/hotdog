from rest_framework import serializers
from .models import Task, TaskHistory


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
    
    def validate(self, attrs):
        if not attrs['fields_of_study'] and not attrs['course']:
            raise serializers.ValidationError("Either field_of_study or course must be provided.")
        return attrs
    

class TaskHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskHistory
        fields = '__all__'