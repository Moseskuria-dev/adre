# accounts/urls.py

from django.urls import path
from .views import login_view, register_view, custom_logout

urlpatterns = [
    
    path('', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', custom_logout, name='logout'),
    # Add other paths for your app's functionality
]
