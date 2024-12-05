from django.db import models


class Booking(models.Model):
    start_dt = models.DateTimeField()
    end_dt = models.DateTimeField()

    room = models.ForeignKey(
        'room.Room',
        on_delete=models.PROTECT,
        related_name='bookings',
    )

    client = models.ForeignKey(
        'user.ClientUser',
        on_delete=models.PROTECT,
        related_name='bookings',
    )
    # review = models.ForeignKey()

    def __str__(self):
        return f'{self.room} ({self.start_dt} - {self.end_dt})'
