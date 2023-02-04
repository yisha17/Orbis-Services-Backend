from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.




def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)



class Department(models.Model):
    department_name = models.CharField(max_length=80)


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=120, default="")
    last_name = models.CharField(max_length=120,default="")
    username = models.CharField(max_length=120)
    email = models.EmailField(max_length=100,default="")
    phone = models.CharField(max_length= 20,null= True)
    profile = models.ImageField(upload_to= upload_to, null=True)
    is_verified = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField()
    is_customer = models.BooleanField()
    is_company = models.BooleanField()
    department = models.ForeignKey(Department,on_delete= models.PROTECT)

    def __str__(self) -> str:
        return self.get_username

    def check_staff(self):
        if self.is_customer == False:
            self.is_staff == True
        else:
            self.is_staff == False



    class Meta(AbstractUser.Meta):
       swappable = 'AUTH_USER_MODEL'
    


