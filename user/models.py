""" Users models """

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    
    def __str__(self):
        return self.username
    
    def get_short_name(self):
        return self.username