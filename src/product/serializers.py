from rest_framework import serializers

# from project app
from product.models import (
    Product, ProductImage, ProductVariant,
    ProductVariantPrice, Variant)


class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = '__all__'


class ProductVariantSerializer(serializers.ModelSerializer):
    # variant  = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = ProductVariant
        fields = '__all__'

class ProductVariantPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariantPrice
        fields = '__all__'
        depth = 1
    # def to_representation(self, instance):
    #     response = super().to_representation(instance)
    #     response['product'] = ProductSerializer(instance.product_id).data
    #     return response


class ProductSerializer(serializers.ModelSerializer):
    # product_variants = serializers.StringRelatedField(many=True, read_only=True)
    product_variants = ProductVariantSerializer(many=True, read_only=True)
    product_variant_prices = ProductVariantPriceSerializer(many=True, read_only=True)
    
    class Meta:
        model = Product
        fields = ['title', 'sku', 'description', 'product_variants', 'product_variant_prices']


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'
