import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from tasks.models import Task
from rest_framework import status
from django.utils import timezone

User = get_user_model()


@pytest.mark.django_db
def test_create_task():
    client = APIClient()
    
    # Create a user and authenticate
    user = User.objects.create_user(username="manager1", password="testpass", role="Manager")
    client.force_authenticate(user=user)
    
    # Send request to create a task
    response = client.post("/tasks/tasks/", {
        "title": "Integration Test Task",
        "description": "Testing API behavior",
        "assigned_to": user.id,
        "status": "To Do",
        "priority": "High",
        "due_date": timezone.now().isoformat()
    })
    
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["title"] == "Integration Test Task"

@pytest.mark.django_db
def test_get_tasks():
    client = APIClient()
    
    # Create a user
    user = User.objects.create_user(username="dev1", password="testpass")
    
    # Create a task
    task = Task.objects.create(
        title="Test Task",
        description="Task Description",
        assigned_to=user,
        status="To Do",
        priority="Medium",
        due_date="2025-03-10"
    )
    
    # Authenticate and make a request
    client.force_authenticate(user=user)
    response = client.get("/tasks/tasks/")
    
    assert response.status_code == status.HTTP_200_OK
    assert response.data["results"][0]["title"] == "Test Task"
