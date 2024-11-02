from django.shortcuts import render
from auths.models import SubmittedAssignment

def home(request):
    submissions = SubmittedAssignment.objects.all()

    context = {
        'submissions': submissions,
    }
    return render(request, 'home.html', context)
