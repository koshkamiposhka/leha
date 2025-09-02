from django.contrib import admin
from .models import Tariff, UserSubscription


@admin.register(Tariff)
class TariffAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "duration_days")


@admin.register(UserSubscription)
class UserSubscriptionAdmin(admin.ModelAdmin):
    list_display = ("user", "tariff", "start_date", "end_date")