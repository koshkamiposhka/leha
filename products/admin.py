from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "product_name", "quantity", "price", "created_at")
    list_filter = ("created_at",)
    search_fields = ("product_name", "user__username")