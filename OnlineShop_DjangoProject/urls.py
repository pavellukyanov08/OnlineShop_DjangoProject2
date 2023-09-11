from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # about
    path('about/', include('about.urls')),

    # favourites
    path('favourites/', include('favourites.urls')),

    # authentication
    path('authentication/', include('authentication.urls')),

    # shopping_cart
    path('cart/', include('shopping_cart.urls')),

    # main_page
    path('', include('main_page.urls')),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
