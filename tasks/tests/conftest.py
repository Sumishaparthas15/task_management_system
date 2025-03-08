# tasks/tests/conftest.py
import pytest
import django

@pytest.fixture(scope="session", autouse=True)
def setup_django():
    django.setup()
