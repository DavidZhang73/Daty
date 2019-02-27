from django.urls import path, include

app_name = 'api'

urlpatterns = [
    path('fc/', include('fileCollector.urls', namespace='fc')),
    path('user/', include('user.urls', namespace='user'))
]
