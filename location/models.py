from django.db import models


class Location(models.Model):
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.city}, {self.country}'

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['city', 'country'],
                name='unique_location',
            ),
        ]
