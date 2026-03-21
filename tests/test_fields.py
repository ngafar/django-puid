import pytest

from django_puid.fields import PrefixedUIDField
from tests.models import MyModel


@pytest.mark.django_db
class TestPrefixedUIDField:
    def test_field_generates_value_on_save(self):
        obj = MyModel.objects.create()
        assert obj.uid != ""
        assert obj.uid is not None

    def test_field_has_correct_prefix(self):
        obj = MyModel.objects.create()
        assert obj.uid.startswith("usr_")

    def test_field_random_part_is_numeric(self):
        obj = MyModel.objects.create()
        prefix, random_part = obj.uid.split("_", 1)
        assert random_part.isdigit()

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
