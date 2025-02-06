from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    bio_details = models.TextField()
    profile_photo = models.ImageField(upload_to='profiles/', null=True, blank=True) 