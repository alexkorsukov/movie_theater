from django.views.generic import View
from api.models import Ticket
from api.forms import TicketForm
from api.common import CSRFExemptMixin, do_get, do_post, do_delete


class TicketView(CSRFExemptMixin, View):
    def get(self, request, *args, **kwargs):
        return do_get(request, Ticket, kwargs, ['administrator'])

    def post(self, request, *args, **kwargs):
        return do_post(request, Ticket, TicketForm, kwargs, ['administrator', 'customer'])

    def delete(self, request, *args, **kwargs):
        return do_delete(request, Ticket, kwargs, ['administrator'])
