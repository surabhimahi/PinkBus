from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Route(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class Schedule(models.Model):
    name = models.CharField(max_length=50)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.name} ({self.start_time} - {self.end_time})"
    
class Bus(models.Model):
    bus_no = models.CharField(max_length=20, unique=True)
    bus_name = models.CharField(max_length=50)
    capacity = models.IntegerField()
    
    start_route = models.ForeignKey(Route, related_name='start_buses', on_delete=models.CASCADE)
    end_route = models.ForeignKey(Route, related_name='end_buses', on_delete=models.CASCADE)

    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.bus_name} ({self.bus_no})"

class Seat(models.Model):
    bus = models.ForeignKey(Bus, related_name='seats', on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10)  # e.g., A1, A2
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.bus.bus_no} - {self.seat_number}"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    booking_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} booked {self.seat.seat_number} on {self.bus.bus_no}"


