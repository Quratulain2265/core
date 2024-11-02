from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from auths.models import User

def student_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.filter(email=email).first()
        
        if user and not user.is_staff:
            student_user = authenticate(username=user.username, password=password)
            if student_user:
                login(request, student_user)
                messages.success(request, "Student logged in successfully")
                return redirect('home')
            else:
                messages.error(request, "Invalid password")
        else:
            messages.error(request, "No student account found with this email")
    
    return redirect('home')

def admin_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.filter(email=email, is_staff=True).first()
        if user: 
            admin_user = authenticate(username=user.username, password=password)
            if admin_user:
                login(request, admin_user)
                messages.success(request, "Admin logged in successfully")
                return redirect('/admin/dashboard') 
            else:
                messages.error(request, "Invalid admin password")
        else:
            messages.error(request, "No admin account found with this email")
    
    return redirect('admin_login')


