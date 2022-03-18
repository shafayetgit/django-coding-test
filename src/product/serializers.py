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
    class Meta:
        model = ProductVariant
        fields = '__all__'


class ProductVariantPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariantPrice
        fields = '__all__'

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

# def search_product(request):
#     title = request.GET.get('title')
#     variant = request.GET.get('variant')
#     price_from = request.GET.get('price_from')
#     price_to = request.GET.get('price_to')
#     date = request.GET.get('date')

#     if title:
#         products = Product.objects.filter(title__icontains=title)
#     elif variant:
#         products = Product.objects.filter(product_variants__variant__id=variant)
#     elif price_from and price_to:
#         products = Product.objects.filter(product_variant_prices__price__gte=int(price_from), product_variant_prices__price__lte=int(price_to))
#     elif price_from:
#         products = Product.objects.filter(product_variant_prices__price__gte=int(price_from))
#     elif price_to:
#         products = Product.objects.filter(product_variant_prices__price_lte=int(price_to))
#     elif date:
#         products = Product.objects.filter(created_at=date) | Product.objects.filter(created_at__gte=date)
#     else:
#         return redirect('product:list.product')


#     context = {
#          'total_records': products.count,
#          'products': products,
#          'variants': Variant.objects.all()

#     }
#     return render(request, 'products/list.html', context)