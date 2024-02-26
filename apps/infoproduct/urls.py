from django.urls import path
from .views import *


urlpatterns = [
    path('categories/', ProductListView.as_view(), name='product_list'),
    path('category/<slug:category_slug>/', ProductListView.as_view(), name='products_by_category'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]