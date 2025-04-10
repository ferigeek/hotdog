from datetime import datetime
from rest_framework import serializers
from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

    def validate(self, data):
        if data['semester'] < 1 or data['semester'] > 2:
            raise serializers.ValidationError("Semester must be either 1 or 2.")
        if data['year'] < (datetime.now().year - 1) or data['year'] > (datetime.now().year + 1):
            raise serializers.ValidationError("Invalid year.")
        return data