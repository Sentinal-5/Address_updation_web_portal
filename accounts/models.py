from django.db import models


# Create your models here.
class Users(models.Model):
    aadhar_num = models.IntegerField(max_length=12, unique=True)
    ph_number = models.IntegerField(max_length=10)

    def __str__(self):
        if self.aadhar_num:
            return self.aadhar_num
        else:
            return self.ph_number
