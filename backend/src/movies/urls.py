from django.urls import path

from . import views

urlpatterns = [
    path('lpv/', views.lpv, name='lpv'),
]