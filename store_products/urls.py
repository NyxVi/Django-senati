""" central store_products Urls. """

# Django
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    # Admin    
    path('admin/', admin.site.urls),

    # Product
    path('products/', include(('products.urls','products'), namespace='product')),
    
    # Sales
    path('sales/', include(('sales.urls','sales'), namespace='sale')),
    
    # Users
    path('users/', include(('user.urls','user'), namespace='user')),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



