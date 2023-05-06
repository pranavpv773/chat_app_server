from django.db import models
# Create your models here.

class EmailOtpData(models.Model):
    otp = models.CharField(max_length=40,blank=True,null=True)
    is_verified=models.BooleanField(default=False)