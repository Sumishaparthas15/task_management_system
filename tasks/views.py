from rest_framework.response import Response
from rest_framework import status, generics
from django.contrib.auth import get_user_model
from .serializers import UserRegistrationSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import *
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from .permissions import IsManagerOrAssignedUser
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import PermissionDenied

User = get_user_model()

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
class UserLoginView(TokenObtainPairView):
    pass  


class TaskPagination(PageNumberPagination):
    page_size = 10

# List & Create Task
class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    pagination_class = TaskPagination
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Allow only Managers to create tasks"""
        if self.request.user.role != "Manager":
            raise PermissionDenied("Only managers can create tasks.")
        serializer.save()

# Retrieve, Update & Delete Task
class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.filter(is_deleted=False)  # Filter out deleted tasks
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsManagerOrAssignedUser]

    def perform_destroy(self, instance):
        """Soft delete task"""
        instance.is_deleted = True
        instance.save()

# List Comments for a Task
class TaskCommentListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskCommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        task_id = self.kwargs["task_id"]
        return TaskComment.objects.filter(task_id=task_id)

    def perform_create(self, serializer):
        task = get_object_or_404(Task, id=self.kwargs["task_id"])
        serializer.save(task=task, author=self.request.user)
