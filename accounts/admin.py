from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (
            "Profile Info",
            {
                "fields": (
                    "phone_number",
                    "profile_picture",
                    "designation",
                    "bio",
                    "address",
                )
            },
        ),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Profile Info",
            {
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "phone_number",
                    "profile_picture",
                    "designation",
                    "bio",
                    "address",
                )
            },
        ),
    )

