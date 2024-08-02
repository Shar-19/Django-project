# models.py

from django.db import models
from django.contrib.auth.models import User

class Flight(models.Model):
    airline_name = models.CharField(max_length=50)
    departure_city = models.CharField(max_length=50)
    arrival_city = models.CharField(max_length=50)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    seats_available = models.IntegerField()

    def __str__(self):
        return f"{self.airline_name} - {self.departure_city} to {self.arrival_city}"

class Passenger(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Reservation(models.Model):
    reservation_date = models.DateTimeField()
    status = models.CharField(max_length=10)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.passenger.first_name} {self.passenger.last_name} - {self.flight}"

class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField()
    payment_method = models.CharField(max_length=50)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)

    def __str__(self):
        return f"Payment of {self.amount} for {self.reservation}"
