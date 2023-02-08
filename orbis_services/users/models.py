from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)



class Department(models.Model):
    department_name = models.CharField(max_length=80)


class CustomUser(AbstractUser):

    first_name = models.CharField(max_length=120, blank=False)
    last_name = models.CharField(max_length=120, blank=False)
    username = models.CharField(max_length=120 , default= "empty")
    email = models.EmailField(max_length=100, blank=False)
    phone = models.CharField(max_length=20, null=False, blank=False,unique=True)
    profile = models.ImageField(upload_to=upload_to, null=True)
    is_verified = models.BooleanField(default=False)
    date_joined = models.DateTimeField(("date joined"), default=timezone.now)
    is_superuser = models.BooleanField(default=False)
    is_employee = models.BooleanField(default= False)
    is_customer = models.BooleanField(default= True)
    is_company = models.BooleanField(default=False)
    is_active = models.BooleanField(("active"), default=True)
    department = models.ForeignKey(
        Department, on_delete=models.PROTECT, null=True)


    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ['username','first_name','last_name','email']

    def __str__(self) -> str:
        return self.first_name

  

    def check_staff(self):
        if self.is_customer == False:
            self.is_staff == True
        else:
            self.is_staff == False

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
