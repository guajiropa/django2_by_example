"""
AUTHOR      :   Robert James Patterson
DATE        :   11/23/18
SYNOPSIS    :   Work thru files for 'Dajngo 2 by Eaxample'
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.url', namespace='blog'))
]
