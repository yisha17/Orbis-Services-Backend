from django.db import models

# Create your models here.


class Cars(models.Model):
    CAR_CHOICES = [
        ('Mercedes','Mercedes'),
        ('Renault','Renault'),
        ('Fuso','Fuso')
    ]

    CAR_TYPES = [
        ('Sedan', 'Sedan'),
        ('Van','Van'),
        ('Bus','Bus')
    ]

    car_model = models.CharField(max_length=120)
    car_brand = models.CharField(max_length=120, choices=CAR_CHOICES)
    car_type = models.CharField(max_length= 80, choices=CAR_TYPES)
    seating_capacity = models.CharField(max_length= 200)
    number_of_door = models.IntegerField()
    payload = models.IntegerField()
   
class Engine(models.model):

    FUEL = [
        ('Petrol','Petrol'),
        ('Diesel','Diesel')
    ]
    car = models.OneToOneField(Cars,on_delete= models.CASCADE,primary_key=True)
    fuel_type = models.CharField(max_length= 120, choices= FUEL)
    car_engine = models.CharField(max_length=120)
    horse_power = models.IntegerField(max=6000)
    emission_standard = models.CharField(max_length=100)


class Transmission(models.model):
    TRANSMISSION = [
        ('Manual','Manual'),
        ('Automatic','Automatic')
    ]
    car = models.OneToOneField(Cars,on_delete= models.CASCADE,primary_key=True)
    gearbox_type =models.CharField(max_length= 120, choices= TRANSMISSION)
    number_of_gears = models.IntegerField()
    transmission = models.CharField(max_length=10)

class AxleAssemblies(models.Model):
    car = models.OneToOneField(Cars,on_delete= models.CASCADE,primary_key=True)
    anti_lock_braking_system = models.BooleanField(default= False)
    servo_brakes = models.CharField(max_length=100)
    wheel_rim_type = models.CharField(max_length=100)
    spare_wheel = models.BooleanField(default= False)

class Upholesty(models.model):
    car = models.OneToOneField(Cars,on_delete= models.CASCADE,primary_key=True)
    seats_upholesty = models.CharField(max_length=100)
    seat_trim = models.CharField(max_length=100)


class AirCondtioning(models.model):
    car = models.OneToOneField(Cars,on_delete= models.CASCADE,primary_key=True)
    air_constioning_type = models.CharField(max_length=100)

class Safety(models.model):
    car = models.OneToOneField(Cars,on_delete= models.CASCADE,primary_key=True)
    safety_belts = models.CharField(max_length=100)
    protection_element = models.CharField(max_length=100)

class Alarm(models.model): 
    car = models.OneToOneField(Cars,on_delete= models.CASCADE,primary_key=True)
    safety_belts = models.CharField(max_length=100)

class Dimensions(models.model):
    car = models.OneToOneField(Cars,on_delete= models.CASCADE,primary_key=True)
    length = models.IntegerField()   
    width = models.IntegerField()   
    height = models.IntegerField()   
    wheel_base = models.IntegerField()
    ground_clearance = models.IntegerField()              