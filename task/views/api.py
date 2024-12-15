from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from task import serializers, models, permissions


class TasksView(ListCreateAPIView):
    serializer_class = serializers.TasksSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return models.Task.objects.filter(related_to__in=user.groups.all()).distinct()
    

class TaskView(RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.TaskPermission]
    queryset = models.Task.objects.all()
    lookup_field = 'id'
    serializer_class = 