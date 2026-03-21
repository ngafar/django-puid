from django.db import models

from django_puid.fields import PrefixedUIDField


class MyModel(models.Model):
    uid = PrefixedUIDField(prefix="usr")

    class Meta:
        app_label = "tests"


class MyModelCustomEntropy(models.Model):
    uid = PrefixedUIDField(prefix="usr", entropy=12)

    class Meta:
        app_label = "tests"


class MyModelCustomSeparator(models.Model):
    uid = PrefixedUIDField(prefix="usr", separator="-")

    class Meta:
        app_label = "tests"
