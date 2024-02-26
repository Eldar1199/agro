from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.product.views import *

router = DefaultRouter()
router.register(r'product', ProductViewSet, basename='product')

urlpatterns = [
    path('pro/', include(router.urls)),
    path('products/<slug:category>/', CategoryView.as_view(), name='product-list-by-category'),
]


