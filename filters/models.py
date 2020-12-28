from django.db import models
from core import models as core_models

class Filter(core_models.TimeStampModel):
    image = models.ImageField(upload_to="filter_photo", null=True, blank=True)
    filter_name = models.CharField(max_length = 300)
    store = models.ForeignKey("stores.Store", related_name="filters", on_delete=models.CASCADE)

    def __Str__(self):
        return self.filter_name
