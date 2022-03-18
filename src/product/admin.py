from django.contrib import admin

from product.models import (
    Product, ProductImage, ProductVariant, 
    ProductVariantPrice, Variant)

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(ProductVariant)
admin.site.register(ProductVariantPrice)
admin.site.register(Variant)
