from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product_form/', views.product_form, name='product'),
]