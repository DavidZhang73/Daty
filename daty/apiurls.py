from django.urls import path, include

app_name = 'api'

urlpatterns = [
    path('usergroup/', include('usergroup.urls', namespace='usergroup')),
    path('user/', include('user.urls', namespace='user')),
    path('collection/', include('collection.urls', namespace='collection'))
]
