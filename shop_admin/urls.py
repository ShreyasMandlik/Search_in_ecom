from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.shop_admin_home,name='shop_admin_home')
]