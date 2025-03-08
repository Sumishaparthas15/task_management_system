import pytest
from django.contrib.auth import get_user_model
from tasks.models import Task, TaskComment

User = get_user_model()

@pytest.mark.django_db
def test_create_task():
    user = User.objects.create_user(username="testuser1", password="testpass")
    task = Task.objects.create(
        title="Test Task",
        description="Test Description",
        assigned_to=user,
        status="To Do",
        priority="Medium",
        due_date="2025-03-10"
    )
    assert task.title == "Test Task"
    assert task.assigned_to == user
    assert task.status == "To Do"

@pytest.mark.django_db
def test_create_comment():
    user = User.objects.create_user(username="dev2", password="testpass")
    task = Task.objects.create(
        title="Test Task",
        description="Task Description",
        assigned_to=user,
        status="To Do",
        priority="Medium",
        due_date="2025-03-10"
    )
    comment = TaskComment.objects.create(task=task, author=user, content="This is a comment")
    
    assert comment.task == task
    assert comment.author == user
    assert comment.content == "This is a comment"
