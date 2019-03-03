from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('login', views.LoginAPI.as_view()),
    path('logout', views.LogoutAPI.as_view()),
    path('signin', views.SigninAPI.as_view()),
    path('signin/emailCheck', views.SigninEmailCheckAPI.as_view()),
    path('signin/active/<uuid:uuid>', views.SigninUserActive.as_view()),
    path('forgetPassword', views.ForgetPasswordAPI.as_view()),
    path('forgetPassword/emailCheck', views.ForgetPasswordEmailCheckAPI.as_view()),
    path('forgetPassword/reset', views.ForgetPasswordResetAPI.as_view()),
    path('forgetPassword/reset/<uuid:uuid>', views.ForgetPasswordReset.as_view()),
]
