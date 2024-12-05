from rest_framework import serializers

from .models import Booking


class BookingSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        return attrs

    class Meta:
        model = Booking
        fields = (
            'pk',
            'start_dt',
            'end_dt',
            'room',
        )
