
from django.urls import path
from .import views

urlpatterns = [
    path('cart/', views.show_cart,name='cart'),
    path('add_cart/', views.add_cart,name='add_cart'),
    path('delete/<pk>',views.remove,name= 'delete'),
    path('checkout/',views.checkout,name = 'checkout'),
    path('show_orders/',views.show_orders,name = 'show_orders')
    

]