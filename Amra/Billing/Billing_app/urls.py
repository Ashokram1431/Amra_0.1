from django.urls import path

from . import views

urlpatterns = [
    path('', views.home,name='Home'),
    path('product', views.product,name='Product'),
    path('sales', views.sales,name='Sales'),
    path('addtocart', views.addtocart,name='AddToCart'),
]
