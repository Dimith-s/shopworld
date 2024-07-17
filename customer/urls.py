from django.urls import path
from . import views


urlpatterns = [
    
    path('acount/',views.account,name='account'),
    path('signout/',views.sign_out,name='signout')

]