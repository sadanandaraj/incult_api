from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """Custom User Admiin"""

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "bio",
                    "gender",
                    "birthdate",
                    "superhost",
                    "following_store"
                )
            },
        ),
    )

    list_display = (
        "username",
        "avatar",
        "email",
        "gender",
        "superhost"
    )
    list_filter = ("superhost","gender")
    filter_horizontal = (
       ("following_store",)
    )

@admin.register(models.Relationship)
class RelationshipAdmin(admin.ModelAdmin):
    list_display = ("user",)

    filter_horizontal = (
        "follower","following",
    )
