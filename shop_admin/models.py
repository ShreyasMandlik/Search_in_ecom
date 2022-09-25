import email
from django.db import models

class shopadmin(models.Model):
    id= models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    mobile=models.CharField(max_length=10)
    password=models.CharField(max_length=50)
    Last_Login=models.TextField()
    is_verified=models.BooleanField(default=False)
    upi=models.TextField()