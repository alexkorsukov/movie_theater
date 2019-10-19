from django.views.generic import View
from api.models import Room
from api.forms import RoomForm
from api.common import CSRFExemptMixin, do_get, do_post, do_delete


class RoomView(CSRFExemptMixin, View):
    def get(self, request, *args, **kwargs):
        return do_get(request, Room, kwargs, ['administrator', 'customer'])

    def post(self, request, *args, **kwargs):
        return do_post(request, Room, RoomForm, kwargs, ['administrator'])

    def delete(self, request, *args, **kwargs):
        return do_delete(request, Room, kwargs, ['administrator'])
