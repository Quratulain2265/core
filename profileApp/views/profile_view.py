from django.shortcuts import render,redirect,HttpResponse


def profile(request):
    return render(request,'profile.html')