from django.urls import path, include  
from .views import login_view
from .views import signup_view
from .views import logout_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('login/',login_view.student_login, name='student_login'),
    path('logout/', logout_view.student_logout, name='student_logout'),
    path('admin/login/', login_view.admin_login, name='admin_login'),
    path('signup/',signup_view.handle_signup,name='signup'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
