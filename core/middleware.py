from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse
from django.utils import timezone
import re

from subscriptions.models import UserSubscription


class ActiveSubscriptionMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        

        path = request.path.strip()
        
        print(f"DEBUG PATH: {repr(path)}")

        if re.match(r"^/api/orders", path):
            if not request.user.is_authenticated:
                return JsonResponse({"detail": "Authentication required."}, status=401)

            now = timezone.now()
            has_active = UserSubscription.objects.filter(
                user=request.user, end_date__gte=now
            ).exists()

            if not has_active:
                return JsonResponse(
                    {"detail": "Active subscription required to access orders."},
                    status=403,
                )

        return None
    
    