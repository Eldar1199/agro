from rest_framework.serializers import ModelSerializer
from apps.product.models import *



# class ProductImageSerializer(ModelSerializer):
#     class Meta:
#         model = ProductImage
#         fields = '__all__'



class ProductDetailSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'status', 'title_product', 'address', 'description', 'category', 'price', 'number', 'image']

        

class ProductListSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'price', 'title_product', 'image']



