import pytest
from tasks.models import Task
from tasks.serializers import TaskSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.mark.django_db
def test_task_serializer():
    user = User.objects.create_user(username="dev1", password="testpass")
    task = Task.objects.create(
        title="Task 1",
        description="Task Description",
        assigned_to=user,
        status="To Do",
        priority="Medium",
        due_date="2025-03-10"
    )
    
    serializer = TaskSerializer(task)
    data = serializer.data

    assert data["title"] == "Task 1"
    assert data["status"] == "To Do"
    assert data["priority"] == "Medium"
