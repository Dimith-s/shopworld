from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from . models import Customers

# Create your views here.
def sign_out(request):
    logout(request)
    return redirect('home')

def account(request):
    context = {}
    if request.POST and 'register' in request.POST :
        context ['register']=True
        try:
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            address = request.POST.get('adress')
            phone = request.POST.get('phone')
            # to create user

            user = User.objects.create_user(username = username,password= password,email= email)
            #create custumer account
            customer = Customers.objects.create(name = username,user=user,address=address,phone= phone)

            messages.success(request,'Registration complete')
        except Exception as e:
            error_message = 'duplicate username or invalid input'
            messages.error(request,error_message)
    if request.POST and 'login' in request.POST :
        context['register']=False
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username= username,password= password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'invalid credential')

        

        
    return render(request,'account.html',context)