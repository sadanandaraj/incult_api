from django.db import models
from core import models as core_models
from stores.models import AbstractItem

class Specs(AbstractItem):
    """ Specs model defination"""

    class Meta:
        verbose_name = "Specs"
        ordering = ["created"]

class Photo(core_models.TimeStampModel):
    """Photo model defination"""

    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="products",)
    product = models.ForeignKey(
        "Product", related_name="photos", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.caption

class Product(core_models.TimeStampModel):

    """ Product model defination """

    product_name = models.CharField(max_length=140)
    store = models.ForeignKey("stores.Store",related_name="products", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    catogary = models.ForeignKey("filters.Filter",related_name="products",on_delete=models.SET_NULL, null=True)
    MRP = models.IntegerField()
    selling_price = models.IntegerField()
    offer = models.IntegerField()
    specs = models.ForeignKey("Specs", related_name="products", on_delete=models.SET_NULL,null=True)
    description = models.TextField()
    size = models.CharField(max_length=140)
    colour = models.CharField(max_length=140)
    liked = models.ManyToManyField("users.User", related_name="products", blank=True)

    def __str__(self):
        return self.product_name

    def total_number_of_photos(self):
        return self.photos.count
    
    total_number_of_photos.short_description = "Photos"

LIKE_CHOICES = (("Like","Like"),("Ublike","Unlike"))

class Like(core_models.TimeStampModel):
    user = models.ForeignKey("users.User", on_delete=models.SET_NULL,null=True)
    product = models.ForeignKey("products.Product", on_delete=models.SET_NULL, null=True)
    value = models.CharField(choices=LIKE_CHOICES, max_length=10)

    def __str__(self):
        return f"{self.user}-{self.product}-{self.value}"
