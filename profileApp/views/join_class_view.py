from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from auths.models import *

def join_class(request):
    if not request.user.is_authenticated:
        messages.info(request, "Please log in to join a class.")
        return redirect('home')  

    all_classes = Classroom.objects.all()
    joined_class = request.user.classroom

    students_in_class = User.objects.filter(classroom=joined_class) if joined_class else None
    resources = Resources.objects.filter(classroom=joined_class) if joined_class else None

    if request.method == 'POST' and not joined_class:
        class_id = request.POST.get('class_id')
        classroom = get_object_or_404(Classroom, id=class_id)
        request.user.classroom = classroom
        request.user.save()
        return redirect('join_class')

    context = {
        'all_classes': all_classes,
        'joined_class': joined_class,
        'students_in_class': students_in_class,
        'resources': resources,
    }
    return render(request, 'join_class.html', context)
