from django.db import models

from django_puid.fields import PrefixedUIDField


class MyModel(models.Model):
    uid = PrefixedUIDField(prefix="usr")

    class Meta:
        app_label = "tests"
