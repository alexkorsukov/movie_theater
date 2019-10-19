from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from jose import jwt
from django.contrib.auth.models import User


class CSRFExemptMixin(object):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(CSRFExemptMixin, self).dispatch(*args, **kwargs)


def do_get(request, m, kwargs, groups):
    no_errors = authenticate(request.GET['token'], groups)
    if no_errors != True: return no_errors

    error_msg = ''
    data = False

    pk = kwargs.get('id', None)

    try:
        if pk is None:
            data = list(m.objects.all().values())
        else:
            data = m.objects.values().get(pk=pk)
    except Exception as e:
        error_msg = str(e)

    return send_respond('get', data, error_msg)


def do_post(request, m, mf, kwargs, groups):
    no_errors = authenticate(request.POST['token'], groups)
    if no_errors != True: return no_errors

    error_msg = ''
    data = False
    action = 'add'

    pk = kwargs.get('id', None)

    try:
        if pk is None:
            mdl = m()
        else:
            mdl = m.objects.get(pk=pk)
            action = 'update'

        form = mf(request.POST, instance=mdl)

        if form.is_valid():
            form.save()
        else:
            error_msg = 'Values are invalid ' + str(form)

        mdl.save()
        pk = mdl.id

        data = m.objects.values().get(pk=pk)

    except Exception as e:
        error_msg = str(e)

    return send_respond(action, data, error_msg)


def do_delete(request, m, kwargs, groups):
    no_errors = authenticate(request.GET['token'], groups)
    if no_errors != True: return no_errors

    error_msg = ''
    data = False

    pk = kwargs.get('id', None)

    try:
        m = m.objects.get(pk=pk)
        m.delete()
        data = {'id': pk}
    except Exception as e:
        error_msg = str(e)

    return send_respond('delete', data, error_msg)


def send_respond(action, data, error_msg):
    if error_msg == '':
        res = [{'result': 'true', 'data': data}]
    else:
        res = [{'result': 'false', 'error_message': 'Cannot ' + action + ' a record, error = ' + str(error_msg)}]

    return JsonResponse(res, safe=False)


def authenticate(token, groups):
    error_message = ''

    try:
        decoded_dict = jwt.decode(token, 'seKre8', algorithms=['HS256'])
        username = decoded_dict.get('username', None)
        user = User.objects.get(username=username)

        if not user:
            error_message = 'Authentication failed, error = User not found'

        user_group = user.groups.values_list('name', flat=True).first()

        if user_group not in groups:
            error_message = 'Authentication failed, error = you don\'t have permissions to run this API'

    except Exception as e:
        error_message = str(e)

    if error_message != '':
        return send_respond('get', [], 'Authentication failed,error = ' + error_message)

    return True


