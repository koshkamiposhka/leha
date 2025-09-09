from rest_framework import serializers
from .models import Tariff, UserSubscription


class TariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tariff
        fields = "__all__"


class UserSubscriptionSerializer(serializers.ModelSerializer):
    tariff = serializers.PrimaryKeyRelatedField(queryset=Tariff.objects.all())

    class Meta:
        model = UserSubscription
        fields = "__all__"
        read_only_fields = ("user", "start_date", "end_date")