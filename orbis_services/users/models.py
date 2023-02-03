from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    username = models.CharField(max_length=120,unique=True, default="")
    email = models.EmailField(max_length=100,default="")
    phone = models.CharField(max_length= 20,null= True)
    
    class Meta(AbstractUser.Meta):
       swappable = 'AUTH_USER_MODEL'
    def __str__(self) -> str:
        return self.get_username
