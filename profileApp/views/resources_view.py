from django.shortcuts import render, redirect
from django.contrib import messages
from auths.models import Resources

def resource(request):
    if not request.user.is_authenticated:
        messages.info(request, "Please log in to access courses.")
        return redirect('home') 
    joined_class = request.user.classroom  
    resources = Resources.objects.filter(classroom=joined_class)
    
    context = {
        'resources': resources
    }
    return render(request, 'resources.html', context)
