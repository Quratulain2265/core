from django.shortcuts import redirect, render, HttpResponse
from auths.models import Resources

def resource(request):
    # Assuming joined_class is the current class joined by the user
    joined_class = request.user.classroom  # Modify this based on your current class retrieval method

    # Filter resources based on the current class
    resources = Resources.objects.filter(classroom=joined_class)
    
    context = {
        'resources': resources
    }
    return render(request, 'resources.html', context)
