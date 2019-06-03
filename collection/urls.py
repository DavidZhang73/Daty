from django.urls import path

from . import views
from utils.views import DownloadAllCollectionFileAPI

app_name = 'collection'

urlpatterns = [
    path('', views.CollectionAPI.as_view()),
    path('<uuid:pk>/', views.CollectionDetailAPI.as_view()),
    path('file/', views.CollectionFileAPI.as_view()),
    path('file/<int:pk>/', views.CollectionFileUploadAPI.as_view()),
    path('file/all/', DownloadAllCollectionFileAPI.as_view())
]
