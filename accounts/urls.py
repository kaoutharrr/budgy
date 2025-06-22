from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.signup_view),
    path('signin/', views.signin_view),
    path('users/', views.list_users),  
]