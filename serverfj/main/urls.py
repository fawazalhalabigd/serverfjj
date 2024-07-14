from django.contrib import admin
from django.urls import path , include
from . import views
from rest_framework import routers

# define the router
router = routers.DefaultRouter()
 
# define the router path and viewset to be used
router.register(r'ips', views.IpsViewSet)
router.register(r'mony', views.MonyViewSet)
router.register(r'place', views.PlaceViewSet)
router.register(r'montag', views.MontagViewSet)
router.register(r'employee', views.EmployeeViewSet)
router.register(r'notificate', views.NotificateViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('kefak_jawad/',view=views.jawad,name='jawad')
]
