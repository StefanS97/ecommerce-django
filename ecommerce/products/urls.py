from django.urls import path
from . import views

app_name = 'products'


urlpatterns = [
    path('', views.home, name='home'),
    path('product/', views.product, name='product'),
    path('checkout/', views.checkout, name='checkout'),
]
