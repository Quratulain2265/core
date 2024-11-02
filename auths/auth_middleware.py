from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth.models import AnonymousUser
from auths.models import User

class KeepAdminLoggedInMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated and request.user.is_staff:
            request.session['admin_user'] = request.user.id
        elif 'admin_user' in request.session:
            request.user = User.objects.get(id=request.session['admin_user'])
