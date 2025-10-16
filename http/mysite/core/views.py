from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import json

@csrf_exempt   # disable CSRF for simplicity (⚠ only for learning, not for production)
def user_handler(request):
    # GET method
    if request.method == "GET":
        users = list(User.objects.values("id", "username", "email"))
        return JsonResponse({"message": "GET request received", "users": users}, status=200)

    # POST method → register user if not exists
    elif request.method == "POST":
        try:
            data = json.loads(request.body)  # get JSON data from request
            username = data.get("username")
            email = data.get("email")
            password = data.get("password")

            if not username or not password:
                return JsonResponse({"error": "username and password required"}, status=400)

            # Check if user already exists
            if User.objects.filter(username=username).exists():
                return JsonResponse({"message": "User already exists"}, status=200)

            # Create new user
            user = User.objects.create_user(username=username, email=email, password=password)
            return JsonResponse({"message": "User registered successfully", "user_id": user.id}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

    # PUT method (example)
    elif request.method == "PUT":
        return JsonResponse({"message": "PUT request received"}, status=200)

    # DELETE method (example)
    elif request.method == "DELETE":
        return JsonResponse({"message": "DELETE request received"}, status=200)

    # Other methods
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)
