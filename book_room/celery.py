import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'book_room.settings')

app = Celery('book_room')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'task-every-10-seconds': {
        'task': 'room_booking.tasks.send_booking_confirmation',  # Полный путь к задаче
        'schedule': 1,  # Интервал: каждые 10 секунд
        'args': (16, 16, 16),
    },
    'task-every-morning': {
        'task': 'room_booking.tasks.send_booking_confirmation',
        'args': (16, 16, 16),
        'schedule': crontab(hour=8, minute=0),  # Каждый день в 8:00 утра
    },
}
