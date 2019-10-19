from django import forms
from api.models import Room, Movie, ShowTime, Ticket


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        exclude = ['id', 'created_at', 'modified_at']


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        exclude = ['id', 'created_at', 'modified_at']


class ShowTimeForm(forms.ModelForm):
    class Meta:
        model = ShowTime
        exclude = ['id', 'created_at', 'modified_at']


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        exclude = ['id', 'created_at', 'modified_at']
