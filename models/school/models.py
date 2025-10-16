from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    roll_number = models.IntegerField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} (Roll: {self.roll_number})"


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    employee_id = models.IntegerField(unique=True)
    department = models.CharField(max_length=100)
    salary = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.department}"
