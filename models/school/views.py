from django.shortcuts import render, redirect
from .models import Student, Employee
from .forms import StudentForm, EmployeeForm
from .forms import StudentForm, EmployeeForm


# 🧍 Student CRUD

# GET - Fetch all students
def student_list(request):
    students = Student.objects.all()   # GET all
    return render(request, 'school/student_list.html', {'students': students})


# POST - Create a new student
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()                # Push to DB
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'school/student_form.html', {'form': form})


# 👨‍💼 Employee CRUD

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'school/employee_list.html', {'employees': employees})


def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'school/employee_form.html', {'form': form})
