from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import bcrypt
from .models import User


@csrf_exempt
def create_user(request):
    if request.method == "POST":
        try:
            print("RAW BODY:", request.body)  # DEBUG

            data = json.loads(request.body)
            print("DATA:", data)  # DEBUG

            username = data.get("username")
            password = data.get("password")
            email = data.get("email")

            print("USERNAME:", username)  # DEBUG
            print("PASSWORD:", password)  # DEBUG
            print("EMAIL:", email)  # DEBUG

            # ✅ Validate inputs
            if not username or not password or not email:
                return JsonResponse(
                    {"error": "username, password, email required"},
                    status=400
                )

            # ✅ encoding (will fail if password is None)
            password_bytes = password.encode("utf-8")

            salt = bcrypt.gensalt(rounds=14)
            hashed_password = bcrypt.hashpw(password_bytes, salt)
            hashed_password = hashed_password.decode("utf-8")

            User.objects.create(
                username=username,
                password=hashed_password,
                email=email
            )

            return JsonResponse({"message": "User created successfully!"}, status=201)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Only POST allowed"}, status=405)


def list_users(request):
    users = list(User.objects.values())
    return JsonResponse(users, safe=False)
