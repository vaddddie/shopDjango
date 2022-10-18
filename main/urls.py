from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index.as_view(), name="index"),
    path('prices/', views.shop.as_view(), name="shop"),
]
