from django.urls import path
from .views import index, add_expence


urlpatterns = [
    path('', index),
    path('add-expence/', add_expence),
    
]