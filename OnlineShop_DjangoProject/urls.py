from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('home_page.urls')),

    # about
    path('about/', include('about.urls')),

    # favourites
    path('favourites/', include('favourites.urls')),

    path('compare/', include('prod_comparison.urls')),

    # authentication
    path('authentication/', include('users.urls')),

    # shopping_cart
    path('cart/', include('shopping_cart.urls')),

    # main_page
    path('products/', include('main_page.urls'))
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
