from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from transactions.filters import TransactionFilter
from transactions.models import Transaction
from transactions.serializers import TransactionSerializer


class TransactionViewSet(CreateModelMixin, ListModelMixin, GenericViewSet):
    serializer_class = TransactionSerializer
    filterset_class = TransactionFilter
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering_fields = ["created", "amount"]
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)
