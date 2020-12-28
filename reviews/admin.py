from django.contrib import admin
from . import models

@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):

    """ Review Admin Defination """

    list_display = (
        "user",
        "rating_average",
        "product",
        "review",
        "accuracy",
        "quality",
        "communication",
        "cleanliness",
        "location",
        "value"
    )

    list_filter = (
        "user__username",
        "product__product_name"
    )

    search_fields = (
        "user__username",
        "product__product_name",
    )
