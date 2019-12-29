from django.urls import path

from .views import ArticleListView, ArticleDetailView
from . import views

urlpatterns = [
    path('article/', ArticleListView.as_view()),
    path('article/<pk>', ArticleDetailView.as_view()),
]