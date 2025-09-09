import pytest
from rest_framework.test import APIClient
from users.models import CustomUser
from subscriptions.models import Tariff


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user(db):
    return CustomUser.objects.create_user(username="testuser", password="password123")


@pytest.fixture
def tariff(db):
    return Tariff.objects.create(name="Basic", price=100, duration_days=30)