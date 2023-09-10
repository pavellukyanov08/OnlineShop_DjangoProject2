from django.urls import path
from . import views

# app_name = 'authentication'

urlpatterns = [
    # Auth
    path('signup/', views.signupuser, name='signup'),
    # Logout
    path('lognout/', views.logoutuser, name='logout'),
    # Loginin
    path('login/', views.loginuser, name='login'),

]