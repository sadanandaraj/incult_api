from django.contrib import admin
from django.utils.html import mark_safe
from . import models

class PhotoInline(admin.TabularInline):
    model = models.Photo

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    """ store Admin definition """

    inlines = (
        PhotoInline,
    )

    fieldsets = (
        (
            "Basic Information",
            {
                "fields": (
                    "product_name",
                    "description",
                    "store",
                    "specs",
                    "quantity",
                    "size",
                    "colour"
                )
            },
        ),
        (
            "Cost Information",
            {
                "fields": (
                    "MRP",
                    "selling_price",
                    "offer",
                )
            },
        ),
        ("Product performance",{"fields":("liked",)}),
    )

    list_display = (
        "product_name",
        "store",
        "quantity",
        "selling_price",
        "MRP",
        "total_number_of_photos",

    )

    list_filter = (
        "selling_price",
    )

    search_fields = (
        "product_name",
        "store__name"
    )
    filter_horizontal = ("liked",)

    raw_id_fields = ("store",)

@admin.register(models.Specs)
class SpecsAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="25px" src="{obj.file.url}" />')
    get_thumbnail.short_description = "Thumbnail"

@admin.register(models.Like)
class ListAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "product",
        "value",
    )

    search_fields = ("user__username","name")
