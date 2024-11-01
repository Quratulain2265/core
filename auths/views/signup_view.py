from django.shortcuts import render, redirect
from auths.models import User 
from django.contrib import messages

def handle_signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')         

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('home')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return redirect('home')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('home')

        user = User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, 'User created successfully')
        return redirect('home')
        
    return redirect('home')
