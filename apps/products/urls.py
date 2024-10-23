from django.urls import path
from . import views

urlpatterns =[
    path('', views.PRODUCTLIST.as_view(), name='product-list')
]