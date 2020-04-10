from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from SDGTest import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('SDGTest.urls')),
    
    # path('', include(router.urls))
]
