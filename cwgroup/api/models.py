from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
#test
class User(AbstractUser):
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    

def __str__(self):
    return self.username
