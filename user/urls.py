from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.UserInfoAPI.as_view()),
    path('login', views.LoginAPI.as_view()),
    path('logout', views.LogoutAPI.as_view()),
    path('signin', views.SigninAPI.as_view()),
    path('signin/checkEmail', views.SigninCheckEmailAPI.as_view()),
    path('signin/active/<uuid:uuid>', views.SigninActiveUser.as_view()),
    path('forgetPassword', views.ForgetPasswordAPI.as_view()),
    path('forgetPassword/checkEmail', views.ForgetPasswordCheckEmailAPI.as_view()),
    path('forgetPassword/reset', views.ForgetPasswordResetAPI.as_view()),
    path('forgetPassword/reset/<uuid:uuid>', views.ForgetPasswordReset.as_view()),
    path('test', views.TestAPI.as_view())
]
