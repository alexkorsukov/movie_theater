from django.views.generic import View
from api.models import Movie
from api.forms import MovieForm
from api.common import CSRFExemptMixin, do_get, do_post, do_delete


class MovieView(CSRFExemptMixin, View):
    def get(self, request, *args, **kwargs):
        return do_get(request, Movie, kwargs, ['administrator', 'customer'])

    def post(self, request, *args, **kwargs):
        return do_post(request, Movie, MovieForm, kwargs, ['administrator'])

    def delete(self, request, *args, **kwargs):
        return do_delete(request, Movie, kwargs, ['administrator'])
