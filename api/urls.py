#from django.urls import path, re_path
# from rest_framework import routers, serilizers, viewsets
#from django.conf.urls import include
#from django.contrib.auth.models import User
#from api import views
from django.urls import path
from api import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    
    path('usuario-list/', views.usuarioShow, name="usuario-show"),
    path('usuario-create/', views.usuarioCreate, name="usuario-create"),
    path('usuario-detail/<str:pk>/', views.usuarioRead, name="usuario-read"),
    path('usuario-update/<str:pk>/', views.usuarioUpdate, name="usuario-update"),
    path('usuario-delete/<str:pk>/', views.usuarioDelete, name="usuario-delete"),

    path('rfid-list/', views.rfidShow, name="rfid-show"),
    path('rfid-create/', views.rfidCreate, name="rfid-create"),
    path('rfid-detail/<str:pk>/', views.rfidRead, name="rfid-read"),
    path('rfid-update/<str:pk>/', views.rfidUpdate, name="rfid-update"),
    path('rfid-delete/<str:pk>/', views.rfidDelete, name="rfid-delete"),

    path('temp-list/', views.tempShow, name="temp-show"),
    path('temp-create/', views.tempCreate, name="temp-create"),
    path('temp-detail/<str:pk>/', views.tempRead, name="temp-read"),
    path('temp-update/<str:pk>/', views.tempUpdate, name="temp-update"),
    path('temp-delete/<str:pk>/', views.tempDelete, name="temp-delete"),
]