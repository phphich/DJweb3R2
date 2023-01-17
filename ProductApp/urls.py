from django.contrib import admin
from django.urls import path, include
from ProductApp import views
urlpatterns = [
    path('', views.productapp_home, name='productapp_home'),
    path('testbt', views.testbt, name='testbt'),


]
