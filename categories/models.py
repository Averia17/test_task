from django.utils.translation import gettext_lazy as _
from django.db import models

from core.models import BaseModel


class Category(BaseModel):
    title = models.CharField(_("Title"), max_length=64)
    user = models.ForeignKey(
        "users.User", related_name="categories", on_delete=models.CASCADE
    )

    class Meta:
        app_label = "categories"
        verbose_name_plural = "Categories"
