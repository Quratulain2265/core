from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from auths.models import Classroom, Assignment, Resources, User


@login_required
def join_class(request):
    all_classes = Classroom.objects.all()
    joined_class = request.user.classroom

    # If the user has joined a class, get all students in that class
    students_in_class = User.objects.filter(classroom=joined_class) if joined_class else None
    print(f"Students in class {joined_class}: {students_in_class}")


    if request.method == 'POST' and not joined_class:
        class_id = request.POST.get('class_id')
        classroom = get_object_or_404(Classroom, id=class_id)
        request.user.classroom = classroom
        request.user.save()
        print(f"User {request.user.username} joined classroom: {request.user.classroom}")
        return redirect('join_class')


    context = {
        'all_classes': all_classes,
        'joined_class': joined_class,
        'students_in_class': students_in_class,
    }
    return render(request, 'join_class.html', context)
