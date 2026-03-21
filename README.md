# django-puid

A Django field that generates human-friendly prefixed unique IDs — a readable alternative to UUIDs.

```
usr_lrjk8xq2a3b9f
order_lrjk8xr7z91mk
```

IDs are time-sortable (timestamp in base36) with a cryptographically random suffix, so they're both friendly and collision-resistant.

## Installation

```bash
pip install django-puid
```

## Usage

```python
from django_puid.fields import PrefixedUIDField

class Order(models.Model):
    uid = PrefixedUIDField(prefix="order")
```

This adds a `uid` field that auto-generates on save and does not replace Django's default integer primary key.

## Options

| Parameter | Default | Description |
|---|---|---|
| `prefix` | required | String prepended to the ID |
| `separator` | `"_"` | Character between prefix and ID body |
| `random_length` | `6` | Number of random characters in the suffix |

```python
# Custom separator and length
uid = PrefixedUIDField(prefix="usr", separator="-", random_length=8)
# → usr-lrjk8xq2a3b9f1z
```

## ID format

```
{prefix}{separator}{timestamp_base36}{random_suffix}
      usr _ lrjk8xq 2a3b9f
```

- **Timestamp** — milliseconds since epoch encoded in base36 (~8 chars, grows slowly)
- **Random suffix** — cryptographically random base36 characters (`secrets` module)
