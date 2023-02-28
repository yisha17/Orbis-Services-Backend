from django.db import models
from users.models import CustomUser
# Create your models here.


class Cars(models.Model):

    CAR_CHOICES = [
        ('Mercedes', 'Mercedes'),
        ('Renault', 'Renault'),
        ('Fuso', 'Fuso'),
    ]

    CAR_TYPES = [
        ('Sedan', 'Sedan'),
        ('Van', 'Van'),
        ('Bus', 'Bus'),
        ('Sedan', 'Sedan'),
        ('Crossover', 'Crossover'),
        ('SUV', 'SUV'),
        ('Micro', 'Micro'),
        ('Hatchback', 'Hatchback'),
        ('Electric Car', 'Electric Car'),
        ('Truck', 'Truck')
    ]

    FUEL = [
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel')
    ]

    TRANSMISSION = [
        ('Manual', 'Manual'),
        ('Automatic', 'Automatic')
    ]

    car_model = models.CharField(max_length=120)
    car_brand = models.CharField(max_length=120, choices=CAR_CHOICES)
    car_type = models.CharField(max_length=80, choices=CAR_TYPES)
    seating_capacity = models.CharField(max_length=200)
    number_of_door = models.IntegerField(null=True)
    payload = models.IntegerField(null=True)
    # --------------engine-------------
    fuel_type = models.CharField(max_length=120, choices=FUEL)
    car_engine = models.CharField(max_length=120, null=True)
    horse_power = models.IntegerField()
    emission_standard = models.CharField(max_length=100)
    # --------------transmission-------------
    gearbox_type = models.CharField(
        max_length=120, choices=TRANSMISSION, null=True)
    number_of_gears = models.IntegerField(null=True)
    transmission = models.CharField(max_length=10)
    # --------------axle assemblies-------------
    anti_lock_braking_system = models.BooleanField(default=False)
    servo_brakes = models.CharField(max_length=100, null=True)
    wheel_rim_type = models.CharField(max_length=100, null=True)
    spare_wheel = models.BooleanField(default=False, null=True)
    # --------------air condtioning/ heating-------------
    air_constioning_type = models.CharField(max_length=100, null=True)
    # --------------safety-------------
    seats_upholesty = models.CharField(max_length=100, null=True)
    seat_trim = models.CharField(max_length=100, null=True)
    # --------------locking/alarm-------------
    electromotor_door_locking = models.CharField(max_length=100, null=True)
    # --------------dimensions-------------
    length = models.IntegerField(null=True)
    width = models.IntegerField(null=True)
    height = models.IntegerField(null=True)
    wheel_base = models.IntegerField(null=True)
    ground_clearance = models.IntegerField(null=True)

    # --------------interested users-------------
    interested_users = models.ManyToOneRel(CustomUser,on_delete=models.RESTRICT,null = True)
    quantity = models.IntegerField(default=0)
    
    
class UserReview(models.model):
    review_title = models.CharField(max_length=120)
    review_description = models.CharField(max_length=500)
    reviewer = models.ForeignKey(CustomUser,primary_key=True,on_delete=models.CASCADE)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)


# class Engine(models.model):

#     FUEL = [
#         ('Petrol','Petrol'),
#         ('Diesel','Diesel')
#     ]
#     car = models.OneToOneField(Cars,on_delete= models.CASCADE,primary_key=True)
#     fuel_type = models.CharField(max_length= 120, choices= FUEL)
#     car_engine = models.CharField(max_length=120)
#     horse_power = models.IntegerField(max=6000)
#     emission_standard = models.CharField(max_length=100)


# class Transmission(models.model):
#     TRANSMISSION = [
#         ('Manual','Manual'),
#         ('Automatic','Automatic')
#     ]
#     car = models.OneToOneField(Cars,on_delete= models.CASCADE,primary_key=True)
#     gearbox_type =models.CharField(max_length= 120, choices= TRANSMISSION)
#     number_of_gears = models.IntegerField()
#     transmission = models.CharField(max_length=10)

# class AxleAssemblies(models.Model):
#     car = models.OneToOneField(Cars,on_delete= models.CASCADE,primary_key=True)
#     anti_lock_braking_system = models.BooleanField(default= False)
#     servo_brakes = models.CharField(max_length=100)
#     wheel_rim_type = models.CharField(max_length=100)
#     spare_wheel = models.BooleanField(default= False)

# class Upholesty(models.model):
#     car = models.OneToOneField(Cars,on_delete= models.CASCADE,primary_key=True)
#     seats_upholesty = models.CharField(max_length=100)
#     seat_trim = models.CharField(max_length=100)


# class AirCondtioning(models.model):
#     car = models.OneToOneField(Cars,on_delete= models.CASCADE,primary_key=True)
#     air_constioning_type = models.CharField(max_length=100)

# class Safety(models.model):
#     car = models.OneToOneField(Cars,on_delete= models.CASCADE,primary_key=True)
#     safety_belts = models.CharField(max_length=100)
#     protection_element = models.CharField(max_length=100)

# class Alarm(models.model):
#     car = models.OneToOneField(Cars,on_delete= models.CASCADE,primary_key=True)
#     safety_belts = models.CharField(max_length=100)

# class Dimensions(models.model):
#     car = models.OneToOneField(Cars,on_delete= models.CASCADE,primary_key=True)
#     length = models.IntegerField()
#     width = models.IntegerField()
#     height = models.IntegerField()
#     wheel_base = models.IntegerField()
#     ground_clearance = models.IntegerField()
