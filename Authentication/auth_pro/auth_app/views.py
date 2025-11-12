from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Student

@csrf_exempt
def create_student(request):
    if request.method == "POST":
        data = json.loads(request.body)
        student = Student(
            name=data["name"],
            email=data["email"]
        )
        student.set_password(data["password"])  # hashes manually
        student.save()
        print(data)
        return JsonResponse({"message": "Student created successfully!"})
@csrf_exempt
def student_detail(request, student_id):
    try:
        student = Student.objects.get(id=student_id)
        data = {
            "id": student.id,
            "name": student.name,
            "email": student.email,
        }
        return JsonResponse(data)
    except Student.DoesNotExist:
        return JsonResponse({"error": "Student not found"}, status=404)
@csrf_exempt
def login_student(request):
    try:
        data = json.loads(request.body)
        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            return JsonResponse({"error": "Email and password are required."}, status=400)

        try:
            student = Student.objects.get(email=email)
        except Student.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=404)

        if student.check_password(password):
            return JsonResponse({"message": "Login successful"})
        else:
            return JsonResponse({"error": "Invalid password"}, status=401)

    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON data"}, status=400)
