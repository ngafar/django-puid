import random

from django.db import models


class PrefixedUIDField(models.CharField):
    def __init__(self, prefix: str, *args, **kwargs):
        self.prefix = prefix
        kwargs.setdefault("max_length", 64)
        kwargs.setdefault("unique", True)
        kwargs.setdefault("editable", False)
        kwargs.setdefault("blank", True)
        super().__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        value = getattr(model_instance, self.attname)
        if not value:
            value = f"{self.prefix}_{random.randint(100_000_000, 999_999_999)}"
            setattr(model_instance, self.attname, value)
        return value

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        kwargs["prefix"] = self.prefix
        return name, path, args, kwargs
