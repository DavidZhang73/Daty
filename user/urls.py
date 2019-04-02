from django.urls import path

from . import views

app_name = 'user'

urlpatterns = [
    path('', views.ProfileAPIView.as_view()),
    path('login/', views.LoginAPIView.as_view()),
    path('logout/', views.LogoutAPIView.as_view()),
    path('checkEmail/', views.CheckEmailAPIView.as_view()),
    path('signin/', views.SigninAPIView.as_view()),
    path('forgetPassword/', views.ForgetPasswordAPIView.as_view()),
    path('forgetPasswordReset/', views.ForgetPasswordResetAPIView.as_view()),
    path('changePassword/', views.ChangePasswordAPIView.as_view()),
    path('signinActive/<uuid:uuid>', views.SigninActiveUser.as_view()),
    path('forgetPasswordReset/<uuid:uuid>', views.ForgetPasswordResetAPIView.as_view()),
]
