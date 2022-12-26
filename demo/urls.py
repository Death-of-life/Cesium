# demo/urls.py

from django.urls import path
from . import views

app_name = "demo"
urlpatterns = [
    path('index/', views.index, name='index'),
    path('demo/',views.demo,name='demo'),
    path('cesium',views.cesium,name = 'cesium')
]