from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Building(models.Model):
    id = models.AutoField(primary_key=True)
    building_name = models.CharField(max_length=50)

    def __str__(self):
        name = (' ').join(str(self.building_name).split('_'))
        return name


class Room(models.Model):
    id = models.AutoField(primary_key=True)
    room_name = models.CharField(max_length=50) 
    building = models.ForeignKey(Building, on_delete=models.CASCADE)

    def __str__(self):
        return self.room_name
    


class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    start_hour = models.TimeField(default='08:00:00')
    end_hour = models.TimeField(default='10:00:00')
    marge = models.IntegerField(null=True)

    def __str__(self):
        room = (' ').join(str(self.room).split('_')).title()
        start_date_str = self.start_date.strftime('%B %dth, %Y')
        start_hour_str = self.start_hour.strftime('%H:%M')
        end_hour_str = self.end_hour.strftime('%H:%M')
        return f"{room} booked on {start_date_str} from {start_hour_str} to {end_hour_str}"
    