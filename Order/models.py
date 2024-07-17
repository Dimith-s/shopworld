from django.db import models

# Create your models here.
#model for the order
from customer.models import Customers
from Product.models import Products

class orders(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_COICES = ((LIVE,'live'),(DELETE,'delete'))
    CART_STAGE = 0
    ORDER_CONFIRMED = 1
    ORDER_PROCESSED = 2
    ORDER_CONFIRMED = 3
    ORDER_REJECTED = 4
    STATUS_CHOICE = ((ORDER_CONFIRMED,'order_confirmed'),(ORDER_PROCESSED,'order_processed'),(ORDER_REJECTED,'order_rejected'))
    order_status = models.IntegerField(choices= STATUS_CHOICE,default='CART_STAGE')
    total_price = models.FloatField(default=0)
    owner = models.ForeignKey(Customers,on_delete=models.SET_NULL,null=True,related_name= 'ordered')
    delete_status = models.IntegerField(choices = DELETE_COICES,default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField( auto_now=True)

    def __str__(self):
        return 'order-{}'.format(self.id)
    
    

# model for the order items
class order_item(models.Model):
    product = models.ForeignKey(Products,related_name= 'added_carts' , on_delete=models.SET_NULL,null= True)
    quantity = models.IntegerField()
    owner = models.ForeignKey(orders, related_name='added_items', on_delete=models.CASCADE)
