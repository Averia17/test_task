from django_filters import rest_framework as filters

from transactions.models import Transaction


class TransactionFilter(filters.FilterSet):
    min_amount = filters.NumberFilter(field_name="amount", lookup_expr="gt")
    max_amount = filters.NumberFilter(field_name="amount", lookup_expr="lt")
    created = filters.DateFilter(field_name="created", lookup_expr="contains")
    max_time = filters.TimeFilter(field_name="created", lookup_expr="time__lt")
    min_time = filters.TimeFilter(field_name="created", lookup_expr="time__gt")

    class Meta:
        model = Transaction
        fields = ["created"]
