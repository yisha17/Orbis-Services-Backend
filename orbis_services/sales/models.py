from django.db import models

# Create your models here.


class Cars(models.Model):
    CAR_CHOICES = [
        ('Mercedes','Mercedes'),
        ('Renault','Renault')
    ]

    CAR_TYPES = [
        ('Sedan', 'Sedan')
    ]

    FUEL = []

    TRANSMISSION = []
    
    car_model = models.CharField(max_length=120)
    car_brand = models.CharField(max_length=120, choices=CAR_CHOICES)
    car_type = models.CharField(max_length= 80, choices=CAR_TYPES)
    fuel_type = models.CharField(max_length= 120, choices= FUEL)
    car_engine = models.CharField(max_length=120)
    car_transmission =models.CharField(max_length= 120, choices= TRANSMISSION)
