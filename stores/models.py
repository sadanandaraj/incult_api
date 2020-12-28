from django.db import models
from core import models as core_models

class AbstractItem(core_models.TimeStampModel):
    """ Abstract Item """
    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class StoreType(AbstractItem):
    """ Store type model Defination """

    class Meta:
        verbose_name = "store Type"
        ordering = ["created"]

class Store(core_models.TimeStampModel):

    """ Store Model Defination """

    STORE_OPEN = "open"
    STORE_CLOSE = "close"

    STATUS_CHOICES = ((STORE_OPEN, "Open"), (STORE_CLOSE,"Close"))

    name = models.CharField(max_length=140)
    logo = models.ImageField(upload_to="store_logo", null=True, blank=True)
    description = models.TextField()
    offer = models.CharField(max_length = 300)
    city = models.CharField(max_length=80)
    owner = models.ForeignKey("users.User", related_name="stores", on_delete=models.CASCADE)
    address = models.CharField(max_length=140)
    lat = models.DecimalField(max_digits=10, decimal_places=6, null=True, blank=True)
    lng = models.DecimalField(max_digits=10, decimal_places=6,null=True, blank=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=8)
    follower = models.ManyToManyField("users.User", related_name="store_follower", null=True, blank=True)
    storeType = models.ForeignKey("StoreType", related_name="stores", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    def number_of_followers(self):
        return self.follower.all().count()
