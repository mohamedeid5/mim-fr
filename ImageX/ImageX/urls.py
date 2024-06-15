
from django.contrib import admin
from django.urls import path
from imageApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.home, name='home'),
    path('send-data', views.data, name='send-data')
]
