from django.template.defaulttags import url
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

# app_name = 'authentication'

urlpatterns = [
    # Auth
    path('signup/', views.signupuser, name='signup'),

    # Logout
    path('lognout/', views.logoutuser, name='logout'),

    # Loginin
    path('login/', views.loginuser, name='login'),

    # user profile
    path('profile/', views.user_profile, name='profile'),

    # editing profile
    path('edit_profile/', views.edit_profile, name='edit-profile'),


    # path('profile/', include('django.contrib.auth.urls')),


    path('reset_password/', auth_views.PasswordResetView.as_view(),
         name='reset_password'),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),


    path('password-change/', auth_views.PasswordChangeView.as_view(),
         name='password_change'),
    path('password-change/', auth_views.PasswordChangeView.as_view(),
         name='password_change_done/'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
