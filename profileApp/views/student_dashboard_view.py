from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from auths.models import SubmittedAssignment

@login_required
def student_dashboard(request):
    submissions = SubmittedAssignment.objects.filter(student=request.user)

    context = {
        'submissions': submissions,
    }
    return render(request, 'student_dashboard.html', context)
