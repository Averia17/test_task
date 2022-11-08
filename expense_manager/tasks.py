from datetime import timedelta

from django.core.mail import send_mail
from django.utils import timezone
from celery import shared_task

from core.constants import NUMBER_STATISTICS_WEEKS
from expense_manager import settings
from users.models import User


@shared_task
def send_user_email(user_email, subject, message):
    send_mail(subject, message, settings.EMAIL_HOST_USER, [user_email])


@shared_task
def get_user_statistics():
    from_time = timezone.now() - timedelta(weeks=NUMBER_STATISTICS_WEEKS)
    for user in User.objects.filter(is_active=True):
        transactions = user.transactions.filter(created__gt=from_time)
        message = (
            f"Your current balance {user.balance} \n"
            f"You have {transactions.count()} transactions in last {NUMBER_STATISTICS_WEEKS} week"
        )
        send_user_email.delay(user.email, "Week statistics", message)
