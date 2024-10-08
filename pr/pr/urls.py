"""
URL configuration for pr project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from base import views as base_views
from django.conf import settings
from django.conf.urls.static import static

#from django.http import HttpResponse, HttpResponseNotFound
#from . import views

# def home(request):
#    return HttpResponse("Hello, world. You're at the pr index.")
# jne..

# def custom_404_view(request, exception):
#    return HttpResponseNotFound("Oops! Page not found. Please check the URL.")

#handler404 = 'custom_404_view'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('api/', include('base.api.urls')),
    #path('', home),
    #path('room/', room),
    #path('redis/', views.redis_demo, name='redis_demo'),
    #ff
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = base_views.custom_404_view