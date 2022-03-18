import json
from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from product.models import Variant, Product,ProductVariant
from product.serializers import (
    ProductSerializer, ProductVariantSerializer, 
    ProductVariantPriceSerializer)


class CreateProductView(generic.TemplateView):
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        print(variants)
        context['product'] = True
        context['variants'] = list(variants.all())
        return context

def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product,
        'update': True,
    }
    return render(request, 'products/create.html', context)


def product_list(request):

    product_list = Product.objects.all().order_by('id') 

    page = request.GET.get('page', 1)

    paginator = Paginator(product_list, 2)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    # print(int(products.next_page_number()))

    total_records = paginator.count

    context = {
        'total_records': total_records,
        'products': products,
        'variants': Variant.objects.all()
    }

    return render(request, 'products/list.html', context)



class ProductViewSet(viewsets.ViewSet):

    # permission_classes = [IsAuthenticated]

    def list(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(
            products, many=True, context={'request': request})
        response_dict = {
            'error': False,
            'message': 'All Products List',
            'data': serializer.data,
        }
        return Response(response_dict)

    def create(self, request):
        product = False
        product_variant = False
        # print(request.data)
        product_serializer = ProductSerializer(
            data=request.data['product'], context={'request': request})
        if product_serializer.is_valid():
            product = product_serializer.save()
        else:
            return Response({
                    'error': True,
                    'message': product_serializer.errors,
                })
        if product:
            product_variants = request.data['productVariants']
            for p_variant in product_variants:
                if p_variant['tags']:
                    variant = Variant.objects.get(id=p_variant['option'])
                    for tag in p_variant['tags']:
                        product_variant_serializer = ProductVariantSerializer(data={
                                                            'variant_title': tag,
                                                            'variant': variant.pk,
                                                            'product': product.pk},
                                                            context={'request': request})
                        if product_variant_serializer.is_valid():
                            product_variant = product_variant_serializer.save()
                            print('product variant is saved')
                        else:
                            return Response({
                                    'error': False,
                                    'message': product_variant_serializer.errors,
                                    # 'message': 'product_variant_serializer failed!.',
                                })
        else:
            response_dict = {
                'error': True,
                'message': 'Something went wrong, please try again',
            }                   
            return Response(response_dict)

        product_variant_prices = request.data['productVariantPrices']

        for product_variant_price in product_variant_prices:
            # product_variants = product_variant_price['title'].split('/')
            product_variants = [x for x in product_variant_price['title'].split('/') if x != '']
            print(product_variant_price['title'])
            print(product_variants)
            product_variant_one = False
            product_variant_two = False
            product_variant_three = False
            for product_variant_title in product_variants:
                try:
                    if product_variant_one == False:
                        product_variant_one = ProductVariant.objects.get(variant_title=product_variant_title, product=product)
                    elif product_variant_two == False:
                        product_variant_two = ProductVariant.objects.get(variant_title=product_variant_title, product=product)
                    elif product_variant_three == False:
                        product_variant_three = ProductVariant.objects.get(variant_title=product_variant_title, product=product)
                except:
                    pass
            price = product_variant_price['price']
            stock = product_variant_price['stock']
            product_variant_price_serializer = ProductVariantPriceSerializer(data={
                                    'product_variant_one': product_variant_one.pk if product_variant_one else '',
                                    'product_variant_two': product_variant_two.pk if product_variant_two else '',
                                    'product_variant_three': product_variant_three.pk if product_variant_three else '',
                                    'price': price,
                                    'stock': stock,
                                    'product': product.pk},
                                    context={'request': request})
            if product_variant_price_serializer.is_valid():
                product_variant_price_serializer.save()
            else:
                return Response({
                        'error': False,
                        'message': product_variant_price_serializer.errors,
                        # 'message': 'product_variant_serializer failed!.',
                    })

        response_dict = {
            'error': False,
            'message': 'Data has been successfully saved!.',
        }

        return Response(response_dict)


    def retrieve(self, request, pk=None):
        try:
            if pk is not None:
                product = Product.objects.get(id=pk)
            if product:
                serializer = ProductSerializer(
                    product, context={'request': request})

                serializer_data = serializer.data
                response_dict = {
                    'error': False,
                    'message': 'Data has been retrieved.',
                    'data': serializer_data,
                }
        except Exception as e:
            print(e)
            response_dict = {
                'error': True,
                'message': str(e)
            }
        return Response(response_dict)


def search_product(request):
    title = request.GET.get('title')
    variant = request.GET.get('variant')
    price_from = request.GET.get('price_from')
    price_to = request.GET.get('price_to')
    date = request.GET.get('date')

    redirect('product:list.product')

    if title:
        products = Product.objects.filter(title__icontains=title)
    elif variant:
       products = Product.objects.filter(product_variants__variant__id=variant)
       print(variant)
    elif price_from and price_to:
        products = Product.objects.filter(product_variant_prices__price__gte=int(price_from), product_variant_prices__price__lte=int(price_to))
    elif price_from:
        print(type(price_from))
        products = Product.objects.filter(product_variant_prices__price__gte=int(price_from))
    elif price_to:
        products = Product.objects.filter(product_variant_prices__price_lte=int(price_to))
    elif date:
        products = Product.objects.filter(created_at=date) | Product.objects.filter(created_at__gte=date)
        print(date)
    elif date:
        products = Product.objects.filter(updated_at=date)
    else:
        return redirect('product:list.product')


    context = {
        'total_records': products.count,
        'products': products,
        'variants': Variant.objects.all()
    }
    return render(request, 'products/list.html', context)

       
