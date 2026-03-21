DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

INSTALLED_APPS = [
    "django_puid",
    "tests",
]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
