from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
# from .models import User
from django.contrib.auth.models import User  # Import the built-in User model
# Create your views here.

def userRegister(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['cpassword']
        email = request.POST['email']
        if password == confirm_password:
            user = User.objects.create_user(username=username, password=password, email=email)
           
            return redirect('login')
    return render(request, 'accounts/userRegister.html')

def userLogin(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('userbookdetails')
        else :
            return redirect('login')
        
       
       


    return render(request, 'accounts/userLogin.html')