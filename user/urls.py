from django.urls import path

from . import views

app_name = 'user'

urlpatterns = [
    path('', views.ProfileAPI.as_view()),
    path('changePassword/', views.ChangePasswordAPI.as_view()),
    path('signinActive/<uuid:uuid>', views.SigninActiveUser.as_view()),
    path('forgetPasswordReset/<uuid:uuid>', views.ForgetPasswordReset.as_view()),
]
