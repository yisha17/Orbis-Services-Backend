from django.db import models

# Create your models here.


class Feedback(models.Model):
    SERVICES  = [
        (1,'Garage'),
        (2,'Spare part'),
    ]

    service = models.IntegerField(choices= SERVICES,default=1)
    rating = models.IntegerField(default=1)
    comment = models.CharField(max_length=330)
    date_posted = models.DateTimeField(auto_now_add=True)