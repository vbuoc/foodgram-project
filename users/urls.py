from django.urls import path
from django.contrib.auth import views as auth_views

from users.views import SignUp

urlpatterns = [
    path("signup/", SignUp.as_view(), name="signup"),
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='users/authForm.html'),
        name='login'
    ),
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='users/resetPassword.html'
        ),
        name='password_reset'
    ),
    path(
        'password-change/',
        auth_views.PasswordChangeView.as_view(
            template_name='users/changePassword.html'
        ),
        name='password_change'
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(template_name='users/logout.html'),
        name='logout'
    ),
]