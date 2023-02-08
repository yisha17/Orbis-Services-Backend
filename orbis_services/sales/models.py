from django.db import models

# Create your models here.


class Cars(models.Model):
    CAR_CHOICES = [
        ('Mercedes','Mercedes'),
        ('Renault','Renault')
    ]

    CAR_TYPES = [
        ('Sedan', 'Sedan'),
        ('Van','Van')
    ]

    FUEL = []

    TRANSMISSION = []
    # ------------Description----------
    car_model = models.CharField(max_length=120)
    car_brand = models.CharField(max_length=120, choices=CAR_CHOICES)
    car_type = models.CharField(max_length= 80, choices=CAR_TYPES)
    seating_capacity = models.CharField(max_length= 200)
    number_of_door = models.IntegerField()
    # ------------Engine----------
    fuel_type = models.CharField(max_length= 120, choices= FUEL)
    car_engine = models.CharField(max_length=120)
    horse_power = models.IntegerField()
    emission_standard = models.CharField(max_length=100)
    # ------------Transmission-----
    car_transmission =models.CharField(max_length= 120, choices= TRANSMISSION)
    

    
