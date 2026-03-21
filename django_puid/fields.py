from django.db import models

from django_puid.utils import generate_id


class PrefixedUIDField(models.CharField):
    def __init__(self, prefix: str, random_length: int = 6, separator: str = "_", *args, **kwargs):
        self.prefix = prefix
        self.random_length = random_length
        self.separator = separator
        kwargs.setdefault("max_length", 64)
        kwargs.setdefault("unique", True)
        kwargs.setdefault("editable", False)
        kwargs.setdefault("blank", True)
        super().__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        value = getattr(model_instance, self.attname)
        if not value:
            value = generate_id(self.prefix, self.random_length, self.separator)
            setattr(model_instance, self.attname, value)
        return value

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        kwargs["prefix"] = self.prefix
        kwargs["random_length"] = self.random_length
        kwargs["separator"] = self.separator
        return name, path, args, kwargs
