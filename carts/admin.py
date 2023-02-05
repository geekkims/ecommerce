from django.contrib import admin

from carts.models import Cart, CartItem, Variation

# Register your models here.
class VariationAdmin(admin.ModelAdmin):
    list_display=('product','variation_category','variation_value','is_active','created_date')
    list_editable=('is_active',)
    list_filter=('product','variation_category')


admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Variation,VariationAdmin)