
from rest_framework import generics
from .serializers import TaskSerializer
from app.models import Task

class TaskApiList(generics.ListCreateAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


