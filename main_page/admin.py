from django.contrib import admin
from .models import *

admin.site.register(Menu)
admin.site.register(Category)


class ProductAdmin(admin.ModelAdmin):
    exclude = ('cart_prods',)


admin.site.register(Product, ProductAdmin)

admin.site.register(FavouriteStatus)

admin.site.register(CompareStatus)

admin.site.register(Review)

admin.site.register(ProductAvailability)
