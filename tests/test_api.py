import pytest
from rest_framework.test import APIClient
from users.models import CustomUser
from subscriptions.models import Tariff, UserSubscription
from products.models import Order
from django.utils import timezone
from datetime import timedelta
from rest_framework.authtoken.models import Token
from decimal import Decimal


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user(db):
    return CustomUser.objects.create_user(username="testuser", password="password123")


@pytest.fixture
def auth_client(db, client):
    user = CustomUser.objects.create_user(username="testuser", password="testpass")

    tariff = Tariff.objects.create(name="Basic", price=100, duration_days=30)
    UserSubscription.objects.create(
        user=user,
        tariff=tariff,
        start_date=timezone.now(),
        end_date=timezone.now() + timedelta(days=tariff.duration_days)
    )

    client.login(username="testuser", password="testpass")

    return client, user



@pytest.fixture
def tariff(db):
    return Tariff.objects.create(name="Basic", price=100, duration_days=30)


@pytest.mark.django_db
def test_get_tariffs(api_client, tariff):
    """Проверяем, что возвращается список тарифов"""
    response = api_client.get("/api/tariffs/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["name"] == "Basic"


@pytest.mark.django_db
def test_create_order(auth_client):
    client, user = auth_client

    response = client.post(
        "/api/orders/",
        {"product_name": "Test Product", "quantity": 2, "price": 500},
        format="json"
    )

    assert response.status_code == 201
    data = response.json()
    assert data["product_name"] == "Test Product"
    assert data["quantity"] == 2
    assert Decimal(data["price"]) == Decimal("500.00")

    order = Order.objects.get(id=data["id"])
    assert order.user == user



