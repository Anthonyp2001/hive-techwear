from django.urls import path 
from .import views 

urlpatterns = [
    path('', views.Categorylist.as_view(), name='list-category'),
]