from django.views.generic import View
from api.models import ShowTime
from api.forms import ShowTimeForm
from api.common import CSRFExemptMixin, do_get, do_post, do_delete


class ShowTimeView(CSRFExemptMixin, View):
    def get(self, request, *args, **kwargs):
        return do_get(request, ShowTime, kwargs, ['administrator', 'customer'])

    def post(self, request, *args, **kwargs):
        return do_post(request, ShowTime, ShowTimeForm, kwargs, ['administrator'])

    def delete(self, request, *args, **kwargs):
        return do_delete(request, ShowTime, kwargs, ['administrator'])
