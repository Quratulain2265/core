from django.shortcuts import render, get_object_or_404
from django.contrib import messages 
from auths.models import Assignment, SubmittedAssignment
from django.contrib.auth.decorators import login_required
from django.utils import timezone

@login_required
def assigned_assignments(request):
    # Get the user's joined class
    joined_class = request.user.classroom
    # Filter assignments by the joined class
    assignments = Assignment.objects.filter(classroom=joined_class) if joined_class else []
    
    context = {
        'assignments': assignments
    }
    return render(request, 'assigned_assignment.html', context)

@login_required
def assignment_detail(request, id):
    new_assignment = get_object_or_404(Assignment, id=id)
    assignment_submit = SubmittedAssignment.objects.filter(assignment=new_assignment, student=request.user)
    
   
    # Check if the assignment belongs to the user's current class
    if new_assignment.classroom != request.user.classroom:
        messages.error(request, 'This assignment does not belong to your current class.')
        return redirect('assigned_assignments')

    if new_assignment.due_date and new_assignment.due_date < timezone.now().date():
        messages.error(request, 'The due date for this assignment has passed. You cannot submit it anymore.')
    elif request.method == 'POST':
        content = request.FILES.get('content')
        if content:
            existing_submission = SubmittedAssignment.objects.filter(assignment=new_assignment, student=request.user).exists()
            if existing_submission:
                messages.error(request, 'You have already submitted this assignment.')
            else:
                SubmittedAssignment.objects.create(
                    assignment=new_assignment,
                    student=request.user,
                    content=content,
                    submission_date=timezone.now()
                )
                messages.success(request, 'Assignment submitted successfully.')
    
    context = {
        'new_assignment': new_assignment,
        'submit': assignment_submit,
    }
    return render(request, 'assignment_detail.html', context)
