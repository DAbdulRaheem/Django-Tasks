from django import forms
from .models import Student, Employee

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
