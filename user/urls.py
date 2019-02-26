from django.urls import include, path
from rest_framework import routers
from . import views

app_name = 'user'

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)

urlpatterns = router.urls
