from django.urls import path, include
from .views import *

urlpatterns = [
    
    path('', login, name='login'),  # login view
    path('register/', register, name='register'),  # login view
]