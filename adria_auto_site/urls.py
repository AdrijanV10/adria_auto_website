from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # This tells Django: "Go look inside the 'website' app for URLs"
    path('', include('website.urls')), 
]