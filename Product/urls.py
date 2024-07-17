from django.urls import path
from .  import views


urlpatterns = [
    path('', views.index,name='home'),
    path ('product/',views.list_product,name= 'product'),
    path('product_detail/<pk>',views.product_details,name='product_detail')
    
]