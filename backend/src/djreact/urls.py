from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('api/movie/', include('movies.api.urls')),
    path('movie/', include('movies.urls')),
    path('', views.index, name='index'),
]