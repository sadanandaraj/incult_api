from django.contrib import admin
from django.utils.html import mark_safe
from . import models

@admin.register(models.Filter)
class FilterAdmin(admin.ModelAdmin):
    list_display = (
        "filter_name",
        "get_thumbnail",
        "store"
    )

    list_filter = ("store",)

    search_fields = (
        "filter_name",
        "store__name",
    )

    def get_thumbnail(self,obj):
        return mark_safe(f'<img width="25px" src="{obj.image.url}" />')
