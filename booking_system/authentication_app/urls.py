from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login', views.login_user, name='login_user'),
    path('sign-up', views.register_user, name='register_user'),
    path('logout', views.logout_user, name='logout_user'),
    path('reset-password', auth_views.PasswordResetView.as_view(template_name="authentication_app/reset_password.html"), 
         name="reset_password"),
    path('reset-password-sent', auth_views.PasswordResetDoneView.as_view(template_name="authentication_app/reset_password_sent.html"), 
         name="password_reset_done"),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="authentication_app/set_password.html"), 
         name="password_reset_confirm"),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name="authentication_app/reset_password_complete.html"), 
         name="password_reset_complete"),
]
