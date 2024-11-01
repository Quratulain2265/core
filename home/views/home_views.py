from django.shortcuts import render
from auths.models import SubmittedAssignment

def home(request):
    # Fetch the submissions to pass to the template
    submissions = SubmittedAssignment.objects.all()

    context = {
        'submissions': submissions,
    }
    return render(request, 'home.html', context)
