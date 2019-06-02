from django.urls import path

from . import views

app_name = 'collection'

urlpatterns = [
    path('', views.CollectionAPI.as_view()),
    path('<uuid:pk>/', views.CollectionDetailAPI.as_view())
]
