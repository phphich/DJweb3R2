
from django.contrib import admin
from django.urls import path, include
from ProfileApp import  views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home' ),
    path('productapp/', include('ProductApp.urls')),
    path('profileapp/', include('ProfileApp.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
