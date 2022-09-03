from django.db import models
from users.models import CustomUser,Driver

class Shuttle(models.Model):
    id = models.AutoField(primary_key=True)

    locations = (
        ("airport suisse side", "airport suisse side"),
        ("airport french side", "airport french side"),
        ("private flight", "private flight"),
        ("Novotel Genève Aéroport France", "Novotel Genève Aéroport France"),
        ("M3 Hôtel & Résidence Ferney Geneva Airport", "M3 Hôtel & Résidence Ferney Geneva Airport"),
    )

    Driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    price = models.FloatField()
    date = models.DateField()
    time = models.TimeField()
    pickup_location = models.CharField(max_length=100, choices=locations)
    drop_location = models.CharField(max_length=100,choices=locations)
    total_seats = models.IntegerField()
    seats_available = models.IntegerField(null=True, blank=True,)
    seats_booked = models.IntegerField(null=True, blank=True,default=0)



    def __str__(self):
        return f'Driver : {self.Driver} |  Pickup Location : {self.pickup_location} | Drop Location : {self.drop_location} | Date : {self.date} | Time : {self.time}'

    def save(self, *args, **kwargs):
        self.seats_available = self.total_seats - self.seats_booked
        super().save(*args, **kwargs)


class ShuttleReservation(models.Model):
    shuttle = models.ForeignKey(Shuttle, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    seats_booked = models.IntegerField()


    def __str__(self):
        return f'User : {self.user} | Shuttle : {self.shuttle} | Seats Booked : {self.seats_booked} '

    def save(self, *args, **kwargs):
        self.shuttle.seats_booked += self.seats_booked
        super().save(*args, **kwargs)


    

   
        

        











