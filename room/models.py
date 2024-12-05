from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()

    location = models.ForeignKey(
        'location.Location',
        on_delete=models.PROTECT,
        related_name='rooms',
    )

    def __str__(self):
        return self.name

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'location'],
                name='unique_room_name_in_location',
            ),
        ]
