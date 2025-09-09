from rest_framework import viewsets, permissions
from .models import Tariff, UserSubscription
from .serializers import TariffSerializer, UserSubscriptionSerializer
from datetime import timedelta
from django.utils import timezone


class TariffViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tariff.objects.all()
    serializer_class = TariffSerializer
    permission_classes = [permissions.AllowAny]


class UserSubscriptionViewSet(viewsets.ModelViewSet):
    serializer_class = UserSubscriptionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserSubscription.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        tariff = serializer.validated_data["tariff"]
        start_date = timezone.now()
        end_date = start_date + timedelta(days=tariff.duration_days)
        serializer.save(user=self.request.user, start_date=start_date, end_date=end_date)