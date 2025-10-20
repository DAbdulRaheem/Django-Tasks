from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    roll_number = models.IntegerField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    employee_id = models.IntegerField(unique=True)
    department = models.CharField(max_length=100)
    salary = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
