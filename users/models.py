from django.db import models
from django.contrib.auth.models import AbstractUser
from core import models as core_models
from django.utils.encoding import python_2_unicode_compatible

class User(AbstractUser):
    
    """ Custom User Model """
    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "other"),
    )

    avatar = models.ImageField(upload_to="avatars", null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, null=True, blank=True)
    bio = models.TextField(default="Add your bio...", blank=True)
    birthdate = models.DateField(null=True)
    following_store = models.ManyToManyField("stores.Store",blank=True,related_name="followingStore")
    favs = models.ManyToManyField("products.Product", related_name="favs")
    superhost = models.BooleanField(default=False)

class Relationship(core_models.TimeStampModel):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="relationship")
    follower = models.ManyToManyField(User, blank=True, related_name="relationship1")
    following = models.ManyToManyField(User, blank=True, related_name="relationship2")