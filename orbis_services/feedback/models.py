from django.db import models
from users.models import Department
# Create your models here.


class Feedback(models.Model):
    rating = models.IntegerField(default=1)
    department = models.ForeignKey(Department, on_delete= models.PROTECT)
    comment = models.CharField(max_length=330)
    date_posted = models.DateTimeField(auto_now_add=True)