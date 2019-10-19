from django.views.generic import View
from api.models import ShowTime, Room, Movie
from api.common import CSRFExemptMixin, authenticate, send_respond


class ShowTimeUserView(CSRFExemptMixin, View):
    def get(self, request, *args, **kwargs):
        no_errors = authenticate(request.GET['token'], ['administrator', 'customer'])
        if no_errors != True: return no_errors

        error_msg = ''
        data = False

        pk = kwargs.get('id', None)

        try:
            if pk is None:
                data = []
                tmp = ShowTime.objects.all().values()
                for v in tmp:
                    v['room'] = Room.objects.values().get(pk=v['room_id'])
                    v['movie'] = Movie.objects.values().get(pk=v['movie_id'])
                    data.append(v)
            else:
                data = ShowTime.objects.values().get(pk=pk)
        except Exception as e:
            error_msg = str(e)

        return send_respond('get', data, error_msg)
