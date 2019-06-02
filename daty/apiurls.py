from django.urls import path, include

app_name = 'api'

from utils.views import UploadFileAPI

urlpatterns = [
    path('usergroup/', include('usergroup.urls', namespace='usergroup')),
    path('user/', include('user.urls', namespace='user')),
    path('collection/', include('collection.urls', namespace='collection')),
    path('file/', UploadFileAPI.as_view())
]
