from django.contrib import admin
from . import models

@admin.register(models.List)
class ListAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "name",
        "total_number_of_products"
    )

    filter_horizontal = ("products",)

    search_fields = ("user__username","name")
