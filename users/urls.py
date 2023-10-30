from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# app_name = 'authentication'

urlpatterns = [
    # Auth
    path('signup/', views.signupuser, name='signup'),

    # Logout
    path('lognout/', views.logoutuser, name='logout'),

    # Loginin
    path('login/', views.loginuser, name='login'),

    path('profile/', views.user_profile, name='profile'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)