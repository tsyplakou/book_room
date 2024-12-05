from rest_framework import serializers

from .models import Room
from location.models import Location


class RoomListSerializer(serializers.ModelSerializer):
    city = serializers.ReadOnlyField(source='location.city')
    country = serializers.ReadOnlyField(source='location.country')

    class Meta:
        model = Room
        fields = (
            'pk',
            'name',
            'capacity',
            'city',
            'country',
        )


class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = (
            'pk',
            'name',
            'capacity',
            'location',
        )


class RoomLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = (
            'pk',
            'city',
            'country',
        )


class RoomWithLocationSerializer(serializers.ModelSerializer):
    location = RoomLocationSerializer()

    class Meta:
        model = Room
        fields = (
            'pk',
            'name',
            'capacity',
            'location',
        )
