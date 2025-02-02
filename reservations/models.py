from django.db import models

class Reservation(models.Model):
    RESERVATION_TYPES = [
        ('HOTEL', 'Hotel'),
        ('TRAIN', 'Train'),
        ('FLIGHT', 'Flight'),
    ]
    user_id = models.IntegerField()
    reservation_type = models.CharField(max_length=10, choices=RESERVATION_TYPES)
    reservation_id = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default='PENDING')

    def __str__(self):
        return f"{self.reservation_type} Reservation {self.id}"