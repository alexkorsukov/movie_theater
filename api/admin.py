from django.contrib import admin
from api.models import Room, Movie, ShowTime, Ticket

# Register your models here.
admin.site.register(Room)
admin.site.register(Movie)
admin.site.register(ShowTime)
admin.site.register(Ticket)
