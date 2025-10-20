from django.urls import path
from django.contrib import admin
from blog import views

urlpatterns = [
    path('blog_home/', views.blog_home, name='blog_home'),
    path('blog_about/', views.blog_about, name='blog_about'),
]
