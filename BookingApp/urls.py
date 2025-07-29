from django.urls import path, include
from .views import *

urlpatterns = [
    
    path('', login_view, name='login'),  # login view
    path('register/', register, name='register'),  # register view
    path('home/', home, name='homeview'),  # register view
]