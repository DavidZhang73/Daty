from django.urls import path

from . import views

app_name = 'user'

urlpatterns = [
    path('', views.UserGroupListCreateAPI.as_view()),
    path('<int:id>/', views.UserGroupAPI.as_view()),
    path('type/', views.TypeAPI.as_view()),
    path('list/', views.UserGroupListAPI.as_view())
    # path('user/<int:id>/', views.UserAPI.as_view()),
]
