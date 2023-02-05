from django.db import models
from django.urls import reverse
from store.models import Product

# Create your models here.
class Cart(models.Model):
    cart_id=models.CharField(max_length=255,blank=True)
    date_added=models.DateField(auto_now_add=True)


    def __str__(self):
        return self.cart_id
    

class CartItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    is_active=models.BooleanField(default=True)

    def sub_total(self):
        return self.product.price * self.quantity


    def __str__(self):
        return self.product
    
variation_category_choices=(
    ('color','color'),
    ('size','size'),
  
)


class Variation(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    variation_category =models.CharField(max_length=255,choices=variation_category_choices)
    variation_value=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    created_date=models.DateTimeField(auto_now=True)


    def __unicode__(self):
        return self.product