from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('login', views.LoginAPI.as_view()),
    path('logout', views.LogoutAPI.as_view()),
]
