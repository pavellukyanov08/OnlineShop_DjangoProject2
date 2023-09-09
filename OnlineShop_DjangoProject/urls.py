from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    # main_page
    path('', include('main_page.urls'), name='index'),
    # About
    path('about/', include('about.urls'), name='about'),

    # authentication
    path('authentication/', include('authentication.urls'), name='authentication'),

    # shopping_cart
    path('cart/', include('shopping_cart.urls'), name='cart'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
