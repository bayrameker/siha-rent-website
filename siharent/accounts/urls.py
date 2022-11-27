from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.RegisterUser,name='register'),
    path('login/',views.LoginUser,name='login'),
    path('logout/',views.LogOut,name='logout'),
    path('dashboard/',views.Dashboard,name='dashboard'),
]
