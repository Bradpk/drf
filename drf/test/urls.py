from django.urls import include, path
from rest_framework import routers
from drf.test import views
from .views import *

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('test/user/', UserViewSet.as_view(), name="get_user_details"),
]

urlpatterns += router.urls