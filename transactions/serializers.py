from django.db import transaction
from rest_framework.fields import CurrentUserDefault
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer

from categories.models import Category
from categories.serializers import CategorySerializer
from transactions.models import Transaction
from users.models import User


class TransactionSerializer(ModelSerializer):
    user = PrimaryKeyRelatedField(
        queryset=User.objects.all(), default=CurrentUserDefault(), write_only=True
    )

    class Meta:
        model = Transaction
        fields = (
            "id",
            "amount",
            "category",
            "organization",
            "description",
            "is_deposit",
            "created",
            "user",
        )

    def create(self, validated_data):
        with transaction.atomic():
            user = self.context["request"].user
            trans = super().create(validated_data)
            user.balance += trans.amount if trans.is_deposit else -trans.amount
            user.save()
            return trans
