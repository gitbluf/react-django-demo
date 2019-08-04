from django.urls import include, path
from rest_framework import routers
from . import views

#ROUTER = routers.DefaultRouter()
#ROUTER.register(r'pornstars', views.PornViewSet)

urlpatterns = [
    path('pornstar/', views.PornList.as_view()),
    path('pornstar/<int:pk>/', views.PornDetail.as_view()),
    #path('', include(ROUTER.urls)),
 #   path('api-auth/', include('rest_framework.urls',
  #                            namespace='rest_framework')),
]
