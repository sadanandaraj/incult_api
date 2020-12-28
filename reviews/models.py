from django.db import models
from core import models as core_models

class Review(core_models.TimeStampModel):

    """Review model defination"""

    review = models.TextField()
    accuracy = models.IntegerField()
    quality = models.IntegerField()
    communication = models.IntegerField()
    cleanliness = models.IntegerField()
    location = models.IntegerField()
    value = models.IntegerField()
    user = models.ForeignKey("users.User", related_name="reviews",on_delete=models.CASCADE)
    product = models.ForeignKey("products.Product", related_name="reviews", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.review}-{self.product}"

    def rating_average(self):
        avg = (
            self.accuracy
            + self.communication
            + self.cleanliness
            + self.location
            + self.quality
            + self.value
        ) / 6
        return round(avg, 2)
