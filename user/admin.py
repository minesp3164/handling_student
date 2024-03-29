from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = [
        (None,{"fields": ("username", "password")}),
        (
            "권한", {"fields":(
                "is_active",
                "is_staff",
                "is_superuser",
                )
            },
        ),
        ("일정", {"fields": ("last_login", "date_joined")}),
    ]