from django.urls import path
from . import views

urlpatterns = [
    path('student/<int:student_id>/', views.student_detail, name='student_detail'),
    path('create-student/', views.create_student, name='create_student'),
    path('login-student/', views.login_student, name='login_student'),
]