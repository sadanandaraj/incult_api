from django.db import models
from core import models as core_models

class OrderItem(core_models.TimeStampModel):

    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCELED = "canceled"
    STATUS_REJECTED =  "rejected"

    STATUS_CHOICES = (
        (STATUS_PENDING,"pending"),
        (STATUS_CONFIRMED,"confirmed"),
        (STATUS_CANCELED,"canceled"),
        (STATUS_REJECTED,"rejected")
    )

    item = models.ForeignKey(
        "products.Product", related_name = "oders", on_delete=models.CASCADE
    )
    quantity = models.IntegerField(default=1)
    store = models.ForeignKey("stores.Store", related_name="oders", on_delete=models.CASCADE)
    user = models.ForeignKey("users.User", related_name = "oders", on_delete=models.CASCADE)
    status = models.CharField(max_length=18, choices=STATUS_CHOICES,default=STATUS_PENDING)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.item.product_name}-{self.quantity}"

class Order(core_models.TimeStampModel):
    
    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCELED = "canceled"
    STATUS_REJECTED =  "rejected"

    STATUS_CHOICES = (
        (STATUS_PENDING,"pending"),
        (STATUS_CONFIRMED,"confirmed"),
        (STATUS_CANCELED,"canceled"),
        (STATUS_REJECTED,"rejected")
    )

    user = models.ForeignKey("users.User", related_name="ordered", on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    store = models.ManyToManyField(
        "stores.Store",
        related_name = "ordered"
    )
    ordered = models.BooleanField(default=False)
    status = models.CharField(max_length=18, choices=STATUS_CHOICES, default=STATUS_PENDING)

    def __str__(self):
        return self.user.username

class Orders(core_models.TimeStampModel):
    user = models.ForeignKey("users.User",related_name="ordereds", on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order)



