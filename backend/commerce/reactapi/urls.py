from django.urls import include, path
from rest_framework import routers
from . import views

ROUTER = routers.DefaultRouter()
ROUTER.register(r'pornstars', views.PornViewSet)

urlpatterns = [
    path('', include(ROUTER.urls)),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework')),
]
