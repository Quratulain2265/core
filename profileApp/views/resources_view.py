from django.shortcuts import render
from auths.models import Resources

def resource(request):
    # Get the current user's joined class
    joined_class = request.user.classroom  # Modify this if you retrieve the current class differently

    # Filter resources to only include those associated with the user's joined class
    resources = Resources.objects.filter(classroom=joined_class)
    
    context = {
        'resources': resources
    }
    return render(request, 'resources.html', context)
