from django.urls import path, include
from profileApp.views import profile_view
from profileApp.views import assign_assignment_view
from profileApp.views import student_dashboard_view
from profileApp.views import mark_assignment_view
from django.conf import settings
from django.conf.urls.static import static
from .views import resources_view
from profileApp.views import join_class_view
from profileApp.views import search_view


urlpatterns = [
    path('update/', profile_view.profile, name='profile'),
    path('resources/',resources_view.resource,name='resources'),
    path('assigned-assignments/', assign_assignment_view.assigned_assignments, name='assigned_assignments'),
    path('assignment/<int:id>/',assign_assignment_view.assignment_detail, name='assignment_detail'),
    path('mark-assignment/<int:submission_id>/',mark_assignment_view.mark_assignment, name='mark_assignment'),
    path('student-dashboard/',student_dashboard_view.student_dashboard, name='student_dashboard'),
    path('join-class/', join_class_view.join_class, name='join_class'),
     path('search/',search_view.search, name='search'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


