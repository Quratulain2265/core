from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import render, redirect


def student_logout(request):
    if request.user.is_staff:
        request.session.pop('admin_user_id', None) 
    logout(request)
    messages.info(request, 'You are logged out')
    return redirect('home')