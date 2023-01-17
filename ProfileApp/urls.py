from django.urls import path
from ProfileApp import views
urlpatterns = [
    path('', views.home, name='home'),
    path('hello', views.helloworld, name='hello' ),
    path('firstpage', views.firspage, name='firstpage'),
    path('secondpage', views.secondpage, name='secondpage'),
    path('thirdpage', views.thirdpage, name='thirdpage'),
    path('hnypage', views.hnypage, name='hnypage'),
    path('hnypdf', views.hnypdf, name='hnypdf'),

]