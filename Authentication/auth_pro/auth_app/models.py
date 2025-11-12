from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  # store hashed password

    def set_password(self, raw_password):
        """Hash and store the password."""
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        """Check if given password matches stored one."""
        return check_password(raw_password, self.password)
