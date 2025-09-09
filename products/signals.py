from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order
from bot.utils import send_new_order_notification
import asyncio

@receiver(post_save, sender=Order)
def notify_user_new_order(sender, instance, created, **kwargs):
    if created and instance.user.telegram_id:
        message = f"Вам пришёл новый заказ!\n{instance.product_name} x{instance.quantity}, {instance.price}₽"
        
        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            loop = None
        
        if loop and loop.is_running():
            asyncio.create_task(send_new_order_notification(instance.user.telegram_id, message))
        else:
            asyncio.run(send_new_order_notification(instance.user.telegram_id, message))