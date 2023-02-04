from django.contrib import admin

from store.models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display=('product_name','slug','category','price','stock','is_available','modified_date')
    prepopulated_fields = {'slug': ('product_name',)}



admin.site.register(Product,ProductAdmin)
