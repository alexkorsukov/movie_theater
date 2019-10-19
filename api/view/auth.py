from django.views.generic import View
from api.common import CSRFExemptMixin, send_respond
from jose import jwt
from django.contrib.auth import authenticate


class AuthView(CSRFExemptMixin, View):
    def post(self, request):
        error_msg = ''
        data = False

        try:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            data = {'token': jwt.encode({'username': user.username}, 'seKre8', algorithm='HS256')}

        except Exception as e:
            error_msg = str(e)

        return send_respond('get', data, error_msg)

