from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    designation=models.CharField(max_length=255, blank=True, null=True)
    bio=models.TextField(blank=True, null=True)
    address=models.TextField(blank=True, null=True)
    

    def __str__(self):
        return self.email 

