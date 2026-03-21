import re
import time

import pytest

from django_puid.fields import PrefixedUIDField
from django_puid.utils import base36_encode, generate_id
from tests.models import MyModel, MyModelCustomEntropy, MyModelCustomSeparator

BASE36_PATTERN = re.compile(r"^[0-9a-z]+$")


class TestGenerateId:
    def test_returns_correct_prefix(self):
        uid = generate_id("usr")
        assert uid.startswith("usr_")

    def test_body_is_base36(self):
        uid = generate_id("usr")
        body = uid.split("_", 1)[1]
        assert BASE36_PATTERN.match(body)

    def test_ids_are_unique(self):
        ids = {generate_id("usr") for _ in range(100)}
        assert len(ids) == 100

    def test_ids_are_time_sortable(self):
        id1 = generate_id("usr")
        time.sleep(0.002)
        id2 = generate_id("usr")
        body1 = id1.split("_", 1)[1]
        body2 = id2.split("_", 1)[1]
        assert body1 < body2

    def test_custom_entropy(self):
        uid_low = generate_id("usr", entropy=2)
        uid_high = generate_id("usr", entropy=12)
        body_low = uid_low.split("_", 1)[1]
        body_high = uid_high.split("_", 1)[1]
        assert len(body_high) - len(body_low) == 10

    def test_custom_separator(self):
        uid = generate_id("usr", separator="-")
        assert uid.startswith("usr-")

    def test_default_separator_is_underscore(self):
        uid = generate_id("usr")
        assert uid.startswith("usr_")

    def test_base36_encode_zero(self):
        assert base36_encode(0) == "0"

    def test_base36_encode_known_values(self):
        assert base36_encode(36) == "10"
        assert base36_encode(35) == "z"


@pytest.mark.django_db
class TestPrefixedUIDField:
    def test_field_generates_value_on_save(self):
        obj = MyModel.objects.create()
        assert obj.uid != ""
        assert obj.uid is not None

    def test_field_has_correct_prefix(self):
        obj = MyModel.objects.create()
        assert obj.uid.startswith("usr_")

    def test_field_body_is_base36(self):
        obj = MyModel.objects.create()
        body = obj.uid.split("_", 1)[1]
        assert BASE36_PATTERN.match(body)

    def test_field_values_are_unique(self):
        obj1 = MyModel.objects.create()
        obj2 = MyModel.objects.create()
        assert obj1.uid != obj2.uid

    def test_field_does_not_overwrite_existing_value(self):
        obj = MyModel.objects.create(uid="usr_99999")
        assert obj.uid == "usr_99999"

    def test_field_is_unique_in_db(self):
        field = MyModel._meta.get_field("uid")
        assert field.unique is True

    def test_field_prefix_is_stored(self):
        field = MyModel._meta.get_field("uid")
        assert field.prefix == "usr"

    def test_field_custom_entropy(self):
        obj = MyModel.objects.create()
        default_body = obj.uid.split("_", 1)[1]

        obj2 = MyModelCustomEntropy.objects.create()
        custom_body = obj2.uid.split("_", 1)[1]

        assert len(custom_body) - len(default_body) == 6

    def test_field_custom_separator(self):
        obj = MyModelCustomSeparator.objects.create()
        assert obj.uid.startswith("usr-")

    def test_field_separator_is_stored(self):
        field = MyModelCustomSeparator._meta.get_field("uid")
        assert field.separator == "-"

    def test_field_default_separator_is_underscore(self):
        field = MyModel._meta.get_field("uid")
        assert field.separator == "_"
