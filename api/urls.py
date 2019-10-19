from django.conf.urls import url
from api.view import room, movie, show_time, show_time_user, ticket, auth

urlpatterns = [
    # Rooms
    url(r'^room/$', room.RoomView.as_view()),
    url(r'^room/(?P<id>[\d]+)/$', room.RoomView.as_view()),

    # Movies
    url(r'^movie/$', movie.MovieView.as_view()),
    url(r'^movie/(?P<id>[\d]+)/$', movie.MovieView.as_view()),

    # ShowTimes
    url(r'^show_time/$', show_time.ShowTimeView.as_view()),
    url(r'^show_time/(?P<id>[\d]+)/$', show_time.ShowTimeView.as_view()),

    url(r'^show_time_user/$', show_time_user.ShowTimeUserView.as_view()),
    url(r'^show_time_user/(?P<id>[\d]+)/$', show_time_user.ShowTimeUserView.as_view()),

    # Tickets
    url(r'^ticket/$', ticket.TicketView.as_view()),
    url(r'^ticket/(?P<id>[\d]+)/$', ticket.TicketView.as_view()),

    url(r'^auth/$', auth.AuthView.as_view()),
]
