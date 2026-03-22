# django-puid

A Django field that generates human-friendly prefixed unique IDs — a readable alternative to UUIDs.

```python
acct_lrjk8xr7z91mk     # Stripe-style IDs
cus_lrjk8xq2a3b9f      # instantly self-describing
post_4kp2mzn8q1vx      # readable in logs, URLs, and support tickets
```

IDs are time-sortable (timestamp in base36) with a cryptographically random suffix, so they're both friendly and collision-resistant.

## Installation

```bash
pip install django-puid
```

## Quick Start

```python
from django_puid.fields import PrefixedUIDField

class Customer(models.Model):
    uid = PrefixedUIDField(prefix="cus")
```

The `uid` field auto-generates on save. It sits alongside Django's default integer primary key — it doesn't replace it.

## Why Not UUID?

| | UUID | django-puid |
|---|---|---|
| Readable in logs | ❌ | ✅ |
| Self-describing in URLs | ❌ | ✅ |
| Easy to copy in support tickets | ❌ | ✅ |
| Time-sortable | ❌ | ✅ |
| Collision-resistant | ✅ | ✅ |

UUIDs are collision-resistant but opaque. `f47ac10b-58cc-4372-a567-0e02b2c3d479` tells you nothing at a glance. Prefixed IDs are just as safe — and immediately meaningful.

```python
# UUID
customer_id = "f47ac10b-58cc-4372-a567-0e02b2c3d479"

# django-puid
customer_id = "cus_lrjk8xq2a3b9f"
```

## Options

| Parameter | Default | Description |
|---|---|---|
| `prefix` | required | String prepended to the ID |
| `separator` | `"_"` | Character between prefix and ID body |
| `random_length` | `6` | Number of random characters in the suffix |

## Django Admin

The field is non-editable by default. To display it in the admin as read-only:

```python
from django.contrib import admin

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    readonly_fields = ["uid"]
```

## License

MIT