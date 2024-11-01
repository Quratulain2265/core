from django.shortcuts import render
from django.db.models import Q
from auths.models import *
from django.contrib.auth import get_user_model

User = get_user_model()

def search(request):
    query = request.GET.get('q')
    assignments = classrooms = users = None

    if query:
        # Search in Assignment model
        assignments = Assignment.objects.filter(
            Q(title__icontains=query) |
            Q(subject__icontains=query)
        )
        
        # Search in Classroom model
        classrooms = Classroom.objects.filter(
            Q(department__icontains=query) |
            Q(session__icontains=query)
        )
        
        # Search in User model
        users = User.objects.filter(
            Q(username__icontains=query) |
            Q(email__icontains=query)
        )

    context = {
        'query': query,
        'assignments': assignments,
        'classrooms': classrooms,
        'users': users,
    }
    return render(request, 'search_results.html', context)
