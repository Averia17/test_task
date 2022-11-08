from django.db import transaction
from rest_framework.fields import CurrentUserDefault
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer

from categories.models import Category
from users.models import User


class CategorySerializer(ModelSerializer):
    user = PrimaryKeyRelatedField(
        queryset=User.objects.all(), default=CurrentUserDefault(), write_only=True
    )

    class Meta:
        model = Category
        fields = ("id", "title", "user")
