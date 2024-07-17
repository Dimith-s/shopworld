from django.shortcuts import render
from . models import *
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    featured_product = Products.objects.order_by('-priority')[:4]
    latest_product = Products.objects.order_by('id')[:4]
    context = {
        'featured_products':featured_product,
        'latest_products': latest_product
    }
    return render(request,'index.html',context)

def list_product(request):
    page = 1
    if request.GET:
        page = request.GET.get('page',1)
    product = Products.objects.order_by('priority')
    product_paginator = Paginator(product,2)
    product = product_paginator.get_page(page)
    context = {
        'products': product
    }

    return render(request,'product.html',context)

def product_details(request,pk):
    product = Products.objects.get(pk=pk)
    context = {
        'products':product
    }

    return render(request,'product_detail.html',context)