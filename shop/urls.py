from django.urls import path
from . import views

urlpatterns = [
    path('', views.toko_home, name='shop-home'),
    path('products/', views.products, name='shop-products'),
    path('product/<int:product_id>/', views.product_detail, name='product-detail'),
    path('cart/', views.cart, name='shop-cart'),
    path('about/', views.shop_about, name='shop-about'),
]