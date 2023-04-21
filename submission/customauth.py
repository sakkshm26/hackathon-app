from rest_framework.authentication import BaseAuthentication
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed
import jwt

class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        code = request.META['HTTP_AUTHORIZATION'][7:-1]
        
        if code is None:
            return None
        
        try:
            decoded = jwt.decode(code, options={"verify_signature": False}) 
            code = decoded['username']

            user = User.objects.get(username=code)
        except User.DoesNotExist:
            raise AuthenticationFailed('No Such User')
        return (user, None)