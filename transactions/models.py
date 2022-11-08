from django.utils.translation import gettext_lazy as _
from django.db import models

from categories.models import Category
from core.constants import TRANSACTION_TYPES
from core.models import BaseModel
from users.models import User


class Transaction(BaseModel):
    amount = models.DecimalField(_("Amount"), max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        Category, related_name="transactions", on_delete=models.CASCADE
    )
    organization = models.CharField(_("Organization"), max_length=256)
    description = models.CharField(
        _("Description"), max_length=256, blank=True, null=True
    )
    is_deposit = models.BooleanField(_("Is deposit"), default=True)
    user = models.ForeignKey(
        User, related_name="transactions", on_delete=models.CASCADE
    )

    class Meta:
        app_label = "transactions"
        verbose_name_plural = "Transactions"
