import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status

User = get_user_model()

@pytest.mark.django_db
def test_user_registration():
    client = APIClient()
    response = client.post("/tasks/register/", {
        "username": "testuser1",
        "password": "testpass",
        "role": "Developer"
    })
    
    # ✅ Debugging step: print response if it fails
    if response.status_code != status.HTTP_201_CREATED:
        print(response.data)  # 👀 This will help us debug the issue

    assert response.status_code == status.HTTP_201_CREATED
    assert "id" in response.data
