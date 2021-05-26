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
    path(
        'logout/',
        auth_views.LogoutView.as_view(template_name='users/logout.html'),
        name='logout'
    ),
    path(
        'password-change/',
        auth_views.PasswordChangeView.as_view(
            template_name='users/changePassword.html'
        ),
        name='password_change'
    ),
    path(
        'password-change-done/',
        auth_views.PasswordChangeDoneView.as_view(
            template_name='users/changePasswordDone.html'
        ),
        name='password_change_done'
    ),
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='users/resetPassword.html'
    ),
         name='password_reset'
         ),
    path(
        'password-reset-done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='users/resetPasswordDone.html'
        ),
        name='password_reset_done'
    ),
    path(
        'password-reset-confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='users/resetPasswordConfirm.html'
        ),
        name='password_reset_confirm'
    ),
    path(
        'password_reset_complete/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='users/resetPasswordComplete.html'
        ),
        name='password_reset_complete'
    ),

]
