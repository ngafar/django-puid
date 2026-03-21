from django.db import models

from django_puid.utils import generate_id


class PrefixedUIDField(models.CharField):
    def __init__(self, prefix: str, entropy: int = 6, *args, **kwargs):
        self.prefix = prefix
        self.entropy = entropy
        kwargs.setdefault("max_length", 64)
        kwargs.setdefault("unique", True)
        kwargs.setdefault("editable", False)
        kwargs.setdefault("blank", True)
        super().__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        value = getattr(model_instance, self.attname)
        if not value:
            value = generate_id(self.prefix, self.entropy)
            setattr(model_instance, self.attname, value)
        return value

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        kwargs["prefix"] = self.prefix
        kwargs["entropy"] = self.entropy
        return name, path, args, kwargs
