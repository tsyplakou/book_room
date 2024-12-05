import django_filters
from .models import Room


class RoomFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        field_name="name", lookup_expr="icontains", label="Room Name"
    )
    location_country = django_filters.CharFilter(
        field_name="location_country", lookup_expr="icontains", label="Country"
    )
    location_city = django_filters.CharFilter(
        field_name="location_city", lookup_expr="icontains", label="City"
    )
    capacity = django_filters.NumberFilter(
        field_name="capacity", lookup_expr="gte", label="Minimum Capacity"
    )

    class Meta:
        model = Room
        fields = ['capacity', 'name', 'location_country', 'location_city']
