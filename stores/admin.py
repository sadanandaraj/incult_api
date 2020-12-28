from django.contrib import admin
from . import models
from django.utils.html import mark_safe

@admin.register(models.Store)
class StoreAdmin(admin.ModelAdmin):
    """ store Admin defination """

    fieldsets = (
        ( 
            "Basic Info",
            {"fields": ("name","logo","description","storeType","status")},
        ),
        (
            "Contact Information",
            {
                "fields":(
                    "city",
                    "address",
                    "owner",
                    "lat",
                    "lng",
                )
            },
        ),
        ("Store performance", {"fields":("offer","follower")}),
    )

    list_display = (
        "name",
        "get_thumbnail",
        "number_of_followers",
        "offer",
        "city",
        "owner",
        "status",
        "storeType"
    )

    list_filter = (
        "city",
        "status",
        "storeType",

    )

    search_fields = (
        "name",
        "city",
        "owner__username"
    )

    filter_horizontal = ("follower",)
    raw_id_fields = ("owner",)

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="25px" src="{obj.logo.url}" />')


@admin.register(models.StoreType)
class storeTypeAdmin(admin.ModelAdmin):
    pass

