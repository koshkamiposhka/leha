from django.db import models
from django.conf import settings


class Tariff(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    duration_days = models.PositiveIntegerField() 

    def __str__(self):
        return f"{self.name} ({self.price}₽ / {self.duration_days} дн.)"


class UserSubscription(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="subscriptions"
    )
    tariff = models.ForeignKey(Tariff, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()

    def __str__(self):
        return f"{self.user.username} → {self.tariff.name}"