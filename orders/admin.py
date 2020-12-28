from django.contrib import admin
from . import models

@admin.register(models.OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    filter_horizontal = (
        "store",
        "items",
    )

@admin.register(models.Orders)
class OrdersItemAdmin(admin.ModelAdmin):
    filter_horizontal = ("orders",)
