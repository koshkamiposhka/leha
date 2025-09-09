from rest_framework.routers import DefaultRouter
from .views import TariffViewSet, UserSubscriptionViewSet

router = DefaultRouter()
router.register(r"tariffs", TariffViewSet, basename="tariffs")
router.register(r"subscriptions", UserSubscriptionViewSet, basename="subscriptions")

urlpatterns = router.urls