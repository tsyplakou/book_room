import django_filters
from .models import Booking


class BookingFilter(django_filters.FilterSet):
    start_dt = django_filters.DateTimeFilter(
        field_name="start_dt", lookup_expr="gte", label="Start Date (>=)"
    )
    end_dt = django_filters.DateTimeFilter(
        field_name="end_dt", lookup_expr="lte", label="End Date (<=)"
    )
    room_name = django_filters.CharFilter(
        field_name="room__name", lookup_expr="icontains", label="Room Name"
    )
    client_name = django_filters.CharFilter(
        field_name="client__name", lookup_expr="icontains", label="Client Name"
    )

    class Meta:
        model = Booking
        fields = ['start_dt', 'end_dt', 'room_name', 'client_name']
