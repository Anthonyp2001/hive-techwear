from rest_framework import status
import datetime

from backend.helpers.error_response import error_response
from .models import User

#Add this mixin to the login-requiredclasses.


class CustomLoginRequiredMixin():

     def dispatch(self, request, *args, **kwargs):
          if 'Authorization' not in request.header:
               return error_response('Please set Auth-token.', status.HTTP_401_UNAUTHORIZED)
          
          token = request.headers['Authorization']
          now = datetime.datetime.now()
          login_user = User.Objects.filter(token=token, token_expires_gt=now)
          if len(login_user)==0:
               return error_response('The token is invalid or expired.', status.HTTP_401_UNAUTHORIZED)
          
          request.login_user = login_user[0]
          return super().dispatch(request, *args, **kwargs)