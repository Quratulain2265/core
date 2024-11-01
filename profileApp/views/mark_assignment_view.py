from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from auths.models import SubmittedAssignment, Assignment 

@user_passes_test(lambda u: u.is_staff)
def mark_assignment(request, submission_id):
    submission = get_object_or_404(SubmittedAssignment, id=submission_id)
    
    if request.method == 'POST':
        marks = request.POST.get('marks')
        feedback = request.POST.get('feedback')

        if marks and marks.isdigit():
            submission.marks = int(marks)
            submission.feedback = feedback
            submission.save()
            return redirect('admin_dashboard') 
    user_submissions = SubmittedAssignment.objects.filter(assignment=submission.assignment)
    all_assignments = Assignment.objects.all()
    context = {
        'submission': submission,
        'user_submissions': user_submissions,
        'all_assignments': all_assignments,  
    }
    return render(request, 'mark_assignment.html', context)
