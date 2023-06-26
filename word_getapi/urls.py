from django.urls import path
from .views import WordGetApi

urlpatterns = [
    path('', WordGetApi.as_view(), name='word')
]
