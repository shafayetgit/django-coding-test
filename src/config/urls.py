from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.decorators.cache import never_cache
from django.views.static import serve

from config import settings

from rest_framework import routers
from product.views import product 

router = routers.DefaultRouter()
router.register('product', product.ProductViewSet, basename='product')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('product/', include('product.urls')),
    path('api/', include(router.urls))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, view=never_cache(serve))
