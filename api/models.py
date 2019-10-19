from django.contrib.auth.models import User
from django.db import models


class BaseModel(models.Model):
    """
    Base Model with default fields
    """
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Room(BaseModel):
    """
    Rooms in a movie theater
    """
    name = models.CharField(max_length=256, unique=True)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name


class Movie(BaseModel):
    """
    Movies
    """
    name = models.CharField(max_length=256, unique=True)
    duration = models.IntegerField()

    def __str__(self):
        return self.name


class ShowTime(BaseModel):
    """
    ShowTimes
    """
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()

    def __str__(self):
        return self.movie.name + ' show time in ' + self.room.name + ' room at ' + str(self.start_datetime)


class Ticket(BaseModel):
    """
    Tickets
    """
    showtime = models.ForeignKey(ShowTime, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return 'Ticket #' + str(self.id) + ' for ' + self.user.first_name
