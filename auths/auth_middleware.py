from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth.models import AnonymousUser
from auths.models import User

class KeepAdminLoggedInMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Check if the user is logged in and is an admin
        if request.user.is_authenticated and request.user.is_staff:
            # Store admin session in a separate session key
            request.session['admin_user'] = request.user.id
        elif 'admin_user' in request.session:
            # Retrieve the admin user without logging them out when students log in/out
            request.user = User.objects.get(id=request.session['admin_user'])
