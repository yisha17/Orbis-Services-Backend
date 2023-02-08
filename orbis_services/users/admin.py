from django.contrib import admin
from .models import CustomUser,Department
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Department)