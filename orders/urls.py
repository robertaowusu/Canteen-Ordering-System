from django.urls import path
from . import views


urlpatterns = [
    path('', views.cart, name='cart'),
    path('track/', views.track_order, name='track_order'),
]
