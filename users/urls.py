from django.contrib import admin
from django.urls import path, include
from .views  import *

urlpatterns = [
    path('users/signup/', signupView.as_view(), name="Signup"),
    path('users/edit/', editUserView.as_view(), name="editUser"),
]