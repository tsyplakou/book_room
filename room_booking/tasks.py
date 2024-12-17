from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def send_booking_confirmation(room_name, start_dt, end_dt):
    send_mail(
        subject='Booking Confirmation',
        message='',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=['teachmeskill.homework@gmail.com'],
        html_message='{} / {} / {}'.format(
            room_name,
            start_dt,
            end_dt,
        ),
    )
