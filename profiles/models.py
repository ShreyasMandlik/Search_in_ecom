from django.db import models


class Profile_Info(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O','Others'),
    )
    id=models.BigAutoField(primary_key=True)
    review=models.TextField()
    # cart_systems=models.ForeignKey(cartsystem,on_delete=models.DO_NOTHING)
    username=models.CharField(max_length=30)
    email=models.EmailField()
    mobile=models.CharField(max_length=10)
    
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    # profile_img=models.ImageField()
    address=models.TextField()