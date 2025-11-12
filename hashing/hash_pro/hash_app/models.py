from django.db import models

# Create your models here.
from django.contrib.auth.hashers import make_password

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True,default="sample@gmail.com")

    def __str__(self):
        return self.username

