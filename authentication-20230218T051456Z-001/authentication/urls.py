from django.contrib import admin
from django.urls import path
from authentication import views

urlpatterns = [
    path("", views.mainfunc.login, name='login'),
    path("signup", views.mainfunc.signup, name='signup'),
    path("dashboard", views.mainfunc.dashboard, name='dashboard'),
    path("wrong", views.mainfunc.wrong, name='wrong'),
    path("correct", views.mainfunc.correct, name='correct'),
    path("login", views.mainfunc.login, name='login'),
    path("password/", views.mainfunc.password, name='password'),
    path("logout/", views.mainfunc.logout, name="logout")
]