from django.shortcuts import render,redirect
from django.contrib import messages
from . models import orders,order_item
from Product.models import Products

# Create your views here.
def show_cart(request):
    user = request.user
    custumer = user.customer_profile
    cart_obj,created = orders.objects.get_or_create(
        owner = custumer,
        order_status = orders.CART_STAGE
    )
    context = {
        'cart': cart_obj
    }
    return render(request,'cart.html',context)
def remove(request,pk):
    item = order_item.objects.get(pk = pk)
    if item:
        item.delete()
    return redirect('cart')
    

def add_cart(request):
    if request.POST:
        user = request.user
        custumer = user.customer_profile
        quantity = int(request.POST.get('quantity'))
        product_id = request.POST.get('productid')
        print('custumer',custumer)
        print('id',product_id)
        print('quantity',quantity)
        cart_obj,created = orders.objects.get_or_create(
            owner = custumer,
            order_status = orders.CART_STAGE
        )
        product = Products.objects.get(pk=product_id)
        ordered_item,created = order_item.objects.get_or_create(
            product = product,
            owner = cart_obj,
            defaults={'quantity': quantity}
            
        )
        if created:
            ordered_item.quantity = quantity 
            ordered_item.save()
        else:
            ordered_item.quantity = ordered_item.quantity + quantity
            ordered_item.save()
    return redirect('cart')

def checkout(request):
    if request.POST:
        user = request.user
        customer = user.customer_profile
        total = float(request.POST.get('total') )
        order_obj = orders.objects.get(
            owner = customer,
            order_status = orders.CART_STAGE
        )
        if order_obj:
            order_obj.order_status = orders.ORDER_CONFIRMED
            order_obj.total_price = total

            order_obj.save()
            status_message = 'your order is processed'
            messages.success(request,status_message)
        else:
            status_message = 'unable to process'
            messages.error(request,status_message)

    return redirect('cart')

def show_orders(request):
    user = request.user
    customer = user.customer_profile
    all_orders = orders.objects.filter(owner=customer).exclude(order_status=orders.CART_STAGE)
    context ={
        'orders':all_orders
    }
    return render(request,'order.html',context)
