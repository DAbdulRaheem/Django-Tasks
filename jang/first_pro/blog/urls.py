from django.urls import path
from . import views

urlpatterns = [
    # Student endpoints
    path('students/', views.student_list_create, name='student_list_create'),
    path('students/<int:pk>/', views.student_detail, name='student_detail'),

    # Employee endpoints
    path('employees/', views.employee_list_create, name='employee_list_create'),
    path('employees/<int:pk>/', views.employee_detail, name='employee_detail'),
]
