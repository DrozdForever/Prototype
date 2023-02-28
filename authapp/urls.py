from . import views
from django.urls import path
from django.contrib.auth import views as authViews

urlpatterns = [
    path('profile', views.profile, name='profile'),
    path('reg/', views.registration, name='registration'),
    path('exit/', authViews.LogoutView.as_view(), name='exit'),
    path('auth/', authViews.LoginView.as_view(
        template_name="authapp/login.html"),
        name='auth'
    ),

    path(
        'pass_reset/',
        authViews.PasswordResetView.as_view(
            template_name='authapp/pass_reset.html'),
        name='pass_reset'
    ),
    path(
        'password_reset_confirm/<uidb64>/<token>/',
        authViews.PasswordResetConfirmView.as_view(
            template_name='authapp/password_reset_confirm.html'),
        name='password_reset_confirm'
    ),
    path(
        'password_reset_done/',
        authViews.PasswordResetDoneView.as_view(
            template_name='authapp/pass_reset_done.html'),
        name='password_reset_done'
    ),

    path(
        'password_reset_complete/',
        authViews.PasswordResetCompleteView.as_view(
            template_name='authapp/password_reset_complete.html'),
        name='password_reset_complete'
    ),
]
